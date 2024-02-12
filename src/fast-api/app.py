import time
import uvicorn
from fastapi import FastAPI
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

app = FastAPI()

# Define API routes
@app.get('/')
def dummy_home():
    # Print the shape of the data
    print("You are in the API home directory")
    # Print the target names
    print(iris.target_names)
    print(iris.data.shape)

@app.get('/data/')
def get_data():
    print(iris.data[:5])
    
if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")