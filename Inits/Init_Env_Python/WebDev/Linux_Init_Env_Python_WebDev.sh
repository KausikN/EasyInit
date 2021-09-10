echo "############### EASY INIT ###############"
echo "# Linux - INIT - ENV - Python - WebDev  #"
echo "#########################################"

# Login as Root User
sudo su

# Install Python - Latest Version
sudo apt-get install -y python

# Pip installs for WebDev
pip install Django
pip install django-rest-framework
pip install Flask
pip install streamlit

echo "#########################################"