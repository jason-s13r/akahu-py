#!/bin/sh

#files=$(find src/akahu/**/*.py | grep -v "__")
files=`find src/akahu/ | grep ".py$" | grep -v "__"`
for file in $files; do
	# Remove the src/akahu/ prefix and .py suffix
	mod=$(echo "$file" | sed 's|src/||; s|\.py$||; s|/|.|g')
	# Get the module name (last part of the path)
	name="${mod}"
	underline="$(echo "$name" | tr "$name" "=")"
	output=$(echo "$file" | sed 's|src/|readthedocs/|; s|\.py$|.rst|')
	echo "Processing: $file as module $mod;"

	if [ -f "$output" ]; then
		echo "SKIP: already exists $output"
		continue
	fi

	echo "CREATE: $output"

	mkdir -p "$(dirname "$output")"
	cat <<FOO > "$output"
${name}
${underline}

.. automodule:: ${mod}
	:members:
	:undoc-members:
	:show-inheritance:
	:inherited-members:
FOO

done