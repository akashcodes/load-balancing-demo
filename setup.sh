sudo apt update
sudo apt upgrade


# install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

# install node 13.8.0
npm install 13.8.0

# install node frameworks
npm install express
npm install pug
npm install node-fetch

sudo apt install python3-pip


# Setup git repo
mkdir load-balancing-demo
cd load-balancing-demo
git init
git config user.email "akashdotcodes@gmail.com"
git config user.name "akashcodes"
git pull https://akashcodes:battlefield%4019@github.com/akashcodes/load-balancing-demo.git master