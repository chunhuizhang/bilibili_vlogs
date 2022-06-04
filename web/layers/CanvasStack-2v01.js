/*=============================================================
  Filename: CanvasStack-2v01.js
  Rev: 2
  By: A.R.Collins
  Description: Utilities to create multiple transparent
  canvas layers suitable for animation.
  License: Released into the public domain
  latest version at
  <http://www/arc.id.au/CanvasLayers.html>

  Date   |Description                                      |By
  -------------------------------------------------------------
  30Oct09 Rev 1.00 First release                            ARC
  08Sep12 bugfix: test for emulator failed in IE9           ARC
  02Mar13 Re-write to use screen canvas as background       ARC
  28Jul13 remove getOverlayCanvas (use getElementById)
          Tidy for JSLint                                   ARC
  20Jul14 Setup a resize handler for layers, required when
          canvas size changes on window resize (width in %).
          Dropped excanvas support                          ARC
  18Sep19 Re-factor to simplify                             ARC
  21Sep19 Convert to Classes etc                            ARC
  30Sep19 Added addResizeCallback method                    
          Released as Rev 2v00                              ARC
  01Jan20 Add Layer.dragObjects to match Cango Layer        ARC 
  =============================================================*/

var CanvasStack;

(function()
{
  "use strict";

  class Layer
  {
    constructor(canvasID, canvasElement)
    {
      this.id = canvasID;
      this.cElem = canvasElement;
      this.dragObjects = [];
    }
  }

  CanvasStack = class{
    constructor(cvsID, stackLimit){
      const savThis = this;

      function setResizeHandler(resizeLayers, timeout){
        let timer_id = undefined;
        window.addEventListener("resize", ()=>{
          if(timer_id != undefined) 
          {
            clearTimeout(timer_id);
            timer_id = undefined;
          }
          timer_id = setTimeout(()=>{
              timer_id = undefined;
              resizeLayers();
              savThis.bkgCanvas.resizeFns.forEach((currFn)=>currFn());
            }, timeout);
        });
      }
            
      function resizeLayers(){
        const t = savThis.bkgCanvas.offsetTop + savThis.bkgCanvas.clientTop,
              l = savThis.bkgCanvas.offsetLeft + savThis.bkgCanvas.clientLeft,
              w = savThis.bkgCanvas.offsetWidth,
              h = savThis.bkgCanvas.offsetHeight;

        // check if canvas size changed when window resized, allow some rounding error in layout calcs
        if ((Math.abs(w - savThis.rawWidth)/w < 0.01) && (Math.abs(h - savThis.rawHeight)/h < 0.01))
        {
          // canvas size didn't change so return
          return;
        }
        // canvas has been resized so resize all the overlay canvases
        for (let j=1; j<savThis.bkgCanvas.layers.length; j++)  // bkg is layer[0]
        {
          let ovl = savThis.bkgCanvas.layers[j].cElem;
          if (ovl)  // may have been deleted so empty slot
          {
            ovl.style.top = t+'px';
            ovl.style.left = l+'px';
            ovl.style.width = w+'px';
            ovl.style.height = h+'px';
            ovl.width = w;    // reset canvas attribute to pixel width
            ovl.height = h;  
          }
        }
      }

      // check if this is a context for an overlay
      if (cvsID.indexOf("_ovl_") !== -1)
      {
        console.error("CanvasStack: canvas must be a background canvas not an overlay");
        return {};
      }
      
      this.cId = cvsID;
      this.stackLimit = stackLimit || 6;
      this.bkgCanvas = document.getElementById(cvsID);
      this.rawWidth = this.bkgCanvas.offsetWidth;   
      this.rawHeight = this.bkgCanvas.offsetHeight;
      this.bkgCanvas.resizeFns = [];

      if (!this.bkgCanvas.hasOwnProperty('layers'))
      {
        // create an array to hold all the overlay canvases for this canvas
        this.bkgCanvas.layers = [];
        // make a Layer object for the bkgCanvas
        let bkgL = new Layer(this.cId, this.bkgCanvas);   // bkgCanvas is always layer[0]
        this.bkgCanvas.layers[0] = bkgL;
        // make sure the overlay canvases always match the bkgCanvas size
        setResizeHandler(resizeLayers, 250);
      }
      if (!this.bkgCanvas.hasOwnProperty('unique'))
      {
        this.bkgCanvas.unique = 0;
      }
    }

    createLayer(){
      const w = this.rawWidth,
            h = this.rawHeight,
            nLyrs = this.bkgCanvas.layers.length;  // bkg is layer 0 so at least 1

      // check background canvas is still there
      if (!(this.bkgCanvas && this.bkgCanvas.layers))
      {
        console.log("CanvasStack: missing background canvas");
        return;
      } 
      if (this.bkgCanvas.layers.length >= this.stackLimit)
      {
        console.error("CanvasStack: too many layers");
        return;
      }
      this.bkgCanvas.unique += 1;     // a private static variable
      const uniqueTag = this.bkgCanvas.unique.toString();
      const ovlId = this.cId+"_ovl_"+uniqueTag;
      const ovlHTML = "<canvas id='"+ovlId+"' style='position:absolute' width='"+w+"' height='"+h+"'></canvas>";
      const topCvs = this.bkgCanvas.layers[nLyrs-1].cElem; 
      topCvs.insertAdjacentHTML('afterend', ovlHTML);
      const newCvs = document.getElementById(ovlId);
      newCvs.style.backgroundColor = "transparent";
      newCvs.style.left = (this.bkgCanvas.offsetLeft+this.bkgCanvas.clientLeft)+'px';
      newCvs.style.top = (this.bkgCanvas.offsetTop+this.bkgCanvas.clientTop)+'px';
      // make it the same size as the background canvas
      newCvs.style.width = this.bkgCanvas.offsetWidth+'px';
      newCvs.style.height = this.bkgCanvas.offsetHeight+'px';
      let newL = new Layer(ovlId, newCvs);
      // save the ID in an array to facilitate removal
      this.bkgCanvas.layers.push(newL);
      
      return ovlId;    // return the new canvas id 
    }

    deleteLayer(ovlyId){
      // check background canvas is still there
      if (!(this.bkgCanvas && this.bkgCanvas.layers))
      {
        console.log("CanvasStack: missing background canvas");
        return;
      } 
      for (let i=1; i<this.bkgCanvas.layers.length; i++)
      {
        if (this.bkgCanvas.layers[i].id === ovlyId)
        {
          let ovlNode = this.bkgCanvas.layers[i].cElem;
          if (ovlNode)
          {
            ovlNode.parentNode.removeChild(ovlNode);
          }
          // now delete layers array element
          this.bkgCanvas.layers.splice(i,1);   // delete the Layer object
        }
      }
    }

    deleteAllLayers(){
      // check background canvas is still there
      if (!(this.bkgCanvas && this.bkgCanvas.layers))
      {
        console.log("CanvasStack: missing background canvas");
        return;
      } 
      for (let i=this.bkgCanvas.layers.length-1; i>0; i--)   // don't delete layers[0] its the bakg canavs
      {
        let ovlNode = this.bkgCanvas.layers[i].cElem;
        if (ovlNode)
        {
          let orphan = ovlNode.parentNode.removeChild(ovlNode);
          orphan = null;
        }
        // now delete layers array element
        this.bkgCanvas.layers.splice(i,1);
      }
      // clear any resize callbacks, the layers are gone
      this.bkgCanvas.resizeFns.length = 0;   // remove any added handlers, leave the basic
    }

    addResizeCallback(callbackFn){
      this.bkgCanvas.resizeFns.push(callbackFn);
    }
  };

}());
