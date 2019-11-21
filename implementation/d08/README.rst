python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

#installing brew42
curl -fsSL https://rawgit.com/kube/42homebrew/master/install.sh | zsh

brew install nginx
sh set_nginxconf.sh
brew services restart nginx
sh start_gunicorn.sh
