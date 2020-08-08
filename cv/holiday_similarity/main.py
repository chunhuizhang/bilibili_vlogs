from cv.holiday_similarity import vis_utils
from cv.holiday_similarity.data_utils import *
from cv.holiday_similarity.prepare_models import e2e_pretrained_network

BATCH_SIZE = 64

triples_data = create_triples(IMAGE_DIR)
split_point = int(len(triples_data) * 0.7)
triples_train, triples_test = triples_data[0:split_point], triples_data[split_point:]

NUM_EPOCHS = 10

image_cache = {}
train_gen = generate_image_triples_batch(triples_train, BATCH_SIZE, shuffle=True)
val_gen = generate_image_triples_batch(triples_test, BATCH_SIZE, shuffle=False)

num_train_steps = len(triples_train) // BATCH_SIZE
num_val_steps = len(triples_test) // BATCH_SIZE

# nn = e2e_network()
nn = e2e_pretrained_network()
history = nn.fit_generator(train_gen,
                           steps_per_epoch=num_train_steps,
                           epochs=NUM_EPOCHS,
                           validation_data=val_gen,
                           validation_steps=num_val_steps)

vis_utils.plot_training_curve(history)
