#!/bin/bash

repo_path="$(dirname "$(realpath "$0")")"

if [[ ":$PATH:" != *":$repo_path/files:"* ]]; then
    echo "export PATH=\"$repo_path/files:\$PATH\"" >> ~/.bashrc
    echo "✅ PATH added ~/.bashrc: $repo_path/files"
fi

if [ -d "$repo_path/files" ]; then
    chmod +x "$repo_path/files"/*
else
    echo "❌files not found!"
    exit 1
fi


source ~/.bashrc


if [ -f "$repo_path/activate.sh" ]; then
    rm -- "$repo_path/activate.sh"
fi

