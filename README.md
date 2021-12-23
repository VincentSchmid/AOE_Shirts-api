<!-- ABOUT THE PROJECT -->
## About The Project
Helper tool to post images of products on instagram or sites like eaby.  
Contains a library, cli and api written in python that removes the background of passed images.  
Background can be set.  

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

for rembg minimum of python 3.8 is required

install dependencies using the provided requirements.txt
The pytorch versions are dependant on which python version you choose and what operating system you are running and the requirements.txt will need to be adjusted accordingly:  
##### mac os:
  ```
  torch==1.10.0+cpu
  torchvision==0.11.1+cpu
  ```
##### linux:
  ```
  torch==1.10.0
  torchvision==0.11.1
  ```

next install the dependecies using:  
  ```sh
  pip install -r requirements.txt
  ```


<!-- USAGE EXAMPLES -->
## Usage CLI

For available parameter execute:

  ```sh
  python shirt_processing_cli.py --help
  ```

The cli file does not add logic and is built on top of the libraries,  
meaning the libraries can be used on their own.  

## Usage API

To run the server execute:

  ```sh
  uvicorn shirt_processing_api:app --reload
  ```

API Documentation available at:
`http://127.0.0.1:8000/docs`
  
## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>
