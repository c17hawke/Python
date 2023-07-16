echo [$(date)]: "START"
export _VERSION_=3.9
echo [$(date)]: "creating environment with python ${_VERSION_}"
conda create --prefix ./env python=${_VERSION_} -y
echo [$(date)]: "add git user"
git config user.name "c17hawke"
git config user.email "sunny.c17hawke@gmail.com"
echo [$(date)]: "activate environment"
source activate ./env
echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "END"

# to remove everything -
# rm -rf env/ .gitignore conda.yaml README.md .git/