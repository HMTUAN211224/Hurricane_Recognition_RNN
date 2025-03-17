import gdown

file_id = "1UbL5a55T8pUgsA-7KmmqAi08sKfsyBfg"
output = "Hurricane_Recognition_RNN.ipynb"

gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
print("Tải xong!")