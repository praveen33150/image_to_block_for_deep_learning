import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_to_blocks(image_path, block_size):
    #Load the image
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    
    #Calculate the number of blocks
    num_blocks_x = width // block_size
    num_blocks_y = height // block_size
    
    #List to store the blocks
    blocks = []
    
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = image[y:y+block_size, x:x+block_size]
            blocks.append(block)
    
    return blocks

def display_blocks(blocks, block_size):
    num_blocks = len(blocks)
    grid_size = int(np.ceil(np.sqrt(num_blocks)))
    
    fig, axes = plt.subplots(grid_size, grid_size, figsize=(10, 10))
    
    for i, block in enumerate(blocks):
        row = i // grid_size
        col = i % grid_size
        axes[row, col].imshow(cv2.cvtColor(block, cv2.COLOR_BGR2RGB))
        axes[row, col].axis('off')
    
    plt.show()

#try
blocks = image_to_blocks("Alan Wake 7.png", 64)
display_blocks(blocks, 64)
