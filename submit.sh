if [ $# != 1 ];                                                                                                                                            then
        echo "usage: submit blogname"
else
        git add .
        git commit -m "$1"
        git push
fi
