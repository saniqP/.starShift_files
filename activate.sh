#!/bin/bash
current_path=$(pwd)
cleaned_path=$(echo "$current_path" | sed 's|/activate.sh||g')

new_path="$cleaned_path/files:$PATH"


export PATH="$new_path"
source ~/.bashrc



if ! grep -q "export PATH=\"$cleaned_path/files:\$PATH\"" ~/.bashrc; then
    echo "export PATH=\"$cleaned_path/files:\$PATH\"" >> ~/.bashrc
    echo "PATH added in ~/.bashrc"
fi

rm activate.sh
