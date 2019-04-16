#! /bin/bash
set -e # exit on first error

push_to_github(){
  echo "push to github ..."
  git push github master
}

push_to_gitee(){
  echo "push to gitee ..."
  git push gitee master
}

main(){
  push_to_github
  push_to_gitee
}

main
