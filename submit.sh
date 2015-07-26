if [ $# != 1 ];                                                                                                                                            then
        echo "usage: submit commitMessage"
else
        git add .
        git commit -m "$1"
        git push
fi
