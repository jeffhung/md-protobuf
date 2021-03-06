md-protobuf provides a generator for generating mardown documnetation files from google protocol buffer files.

# Producing Code

md-protobuf provides a plugin for the _protoc_ protocol buffer compiler (it ships with protocol buffers). This plugin tells _protoc_ to produce a set of mardown output files, which contains documentation derived from the comments in the proto file.

First, obtain a copy of md-protobuf:

    $ git clone git@github.com:mickem/md-protobuf.git
    $ cd md-protobuf

Next, install md-protobuf:

    $ python setup.py install

Finally, launch protoc and tell it to produce Md output:

    $ protoc -I/path/to/your/proto/files --md_out=/output/path file1.proto file2.proto

You simply need to add _--md_out_ to the arguments to _protoc_ to get it to produce the Markdown output files.

Under the hood, _protoc_ is looking for the program _protoc-gen-md_ somewhere in your $PATH. You can modify $PATH in lieux of installing the package, if you desire.
