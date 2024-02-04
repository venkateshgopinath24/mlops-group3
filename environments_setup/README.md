# Setting up MLOps Environments on GCP

This directory includes instructions of how to build MLOps environments on Google Cloud using different 
technology suites.

* [MLOps with Cloud Composer and MLflow](mlops-composer-mlflow).

However, before proceeding, we need to get some basics installed on your local machine. Below are the commands for Mac users.

## Setting up Virtual Environment

1. Install `pyenv` for managing virtual environments \
    `brew install pyenv pyenv-virtualenv`
2. Select the Python version that will be used for the project and configure it. \
    `pyenv install 3.10`
3. Create a directory for your project and navigate to that directory.
4. Execute the following command to create a virtual environment \
   `pyenv virtualenv 3.10 gcpenv`
5. Once the virtual environment is created, restart your terminal.
6. Execute the following commands: \
   `eval "$(pyenv init --path)"` \
   `eval "$(pyenv init -)"` \
   `eval "$(pyenv virtualenv-init -)"`

Now the virtual environment is configured properly, and can be activated using commands: \
`pyenv activate gcpenv`

You should also check your python and pip versions: \
`python --version` \
`pip --version` 

It is recommended that you update your pip version to the latest version: \
`python -m pip install --upgrade pip`

## Installing Google Cloud Dependencies

1. Download the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
2. Extract the tar.gz file into your directory which would create a folder named "google-cloud-sdk"
3. Navigate to the folder, and execute the following command: \
`./google-cloud-sdk/install.sh`
4. This should begin the SDK installation and you may come across the following prompts: \
   - Do you want to help improve the Google Cloud CLI (y/N)?  y
   - Modify profile to update your $PATH and enable shell command completion? \
   Do you want to continue (Y/n)?  Y

5. Now it will prompt you set the path for the bashrc file as:
   - Enter a path to an rc file to update, or leave blank to use `[/Users/debanjansaha/.zshrc]`:
   - Do not have to enter anything here, just press enter and continue
6. Then it will ask you whether you want to install Python 3.11 for best compatibility. It is upto you to decide whether you want to install it or not. I personally preferred version 3.10, so I did not install it.
7. Finally, you have to configure your installation by executing the following commands:
   - For Windows Users:
     - `source ./google-cloud-sdk/path.bash.inc`
     - `source ./google-cloud-sdk/completion.bash.inc`
   - For Mac Users:
     - `source ./google-cloud-sdk/path.zsh.inc`
     - `source ./google-cloud-sdk/completion.zsh.inc`
8. Go to your home directory for me it is `/Users/debanjansaha` and create a new file called `path.zsh.inc` and add the following lines to your file:
```
    script_link="$( readlink "$0" )" || script_link="$0"
    apparent_sdk_dir="${script_link%/*}"
    if [ "$apparent_sdk_dir" == "$script_link" ]; then
    apparent_sdk_dir=.
    fi
    sdk_dir="$( cd -P "$apparent_sdk_dir" && pwd -P )"
    bin_path="$sdk_dir/bin"
    export PATH=$bin_path:$PATH

```

That's it! You can now access the gcloud CLI. Check your installation by running the following command: \
`gcloud --version` which will show that you have the following configuration set up:
   - Google Cloud SDK 462.0.1
   - bq 2.0.101
   - core 2024.01.31
   - gcloud-crc32c 1.0.0
   - gsutil 5.27
