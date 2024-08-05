if [ "${BASH_SOURCE[0]}" -ef "$0" ]
then
    echo "Please source this script instead of executing"
    exit 1
fi
echo "Installing dependencies......"
pip install -r requirements.txt --quiet --exists-action=i
echo "Setting environment variables......"
export TERM=xterm-256color
echo "Done"
