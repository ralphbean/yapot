import os
import sys
import uuid
from yapot import convert_document

def run():
    print "Welcome to yapot!"
    if len(sys.argv) != 2:
        print "Usage:\n\n\tpython cli-tool.py <pdf_filename>\n\n"

    else:
        pdf_filename = sys.argv[1]
        #base_page_name = os.path.expanduser(pdf_filename)

        success, pdf_text = convert_document(
            pdf_filename = pdf_filename,
            #base_page_name = base_page_name,
            resolution = 200,
            delete_files = False, #True,
            page_delineation = '\n--------\n',
            verbose = True,
            #temp_dir = str(uuid.uuid4())
        )

        with open('%s.txt' % pdf_filename, 'w') as f:
            f.write(pdf_text)

        print "Done."

if __name__ == '__main__':

    run()
