# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-gpt2-c1'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

dataset = 'gutenberg'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 32 # context of up to 256 previous characters

n_layer = 9
n_head = 8
n_embd = 96
dropout = 0.0

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 24033
lr_decay_iters = max_iters # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
device = 'cpu'  # run on cpu only
compile = False # do not torch compile the model
