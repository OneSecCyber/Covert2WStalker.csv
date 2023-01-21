import sys
import os



def Convert_2_WStalker_CSV():
    
    with open('.request.xml', 'r') as f1:
        file1_contents = f1.readlines()

    with open('.response.xml', 'r') as f2:
        file2_contents = f2.readlines()

    with open('.method.xml', 'r') as f3:
        file3_contents = f3.readlines()

    with open('.url.xml', 'r') as f4:
        file4_contents = f4.readlines()
    
 
    with open('.combined_file.csv', 'w') as f_out:
        for i in range(max(len(file1_contents), len(file2_contents), len(file3_contents), len(file4_contents))):
            if i < len(file1_contents):
                f_out.write(file1_contents[i].rstrip().replace(" ",""))
            if i < len(file2_contents):
                f_out.write(file2_contents[i].rstrip().replace('<response base64="true"></response>','').replace(" ",""))
            if i < len(file3_contents):
                f_out.write(file3_contents[i].rstrip().replace(" ",""))
            if i < len(file4_contents):
                f_out.write(file4_contents[i].rstrip().replace(" ","")+ "\n" )


    # remove request which does not have response
    def Remove_InCompleted_requests():

        output_file_name = sys.argv[1].replace('.xml','.csv')
        
        with open(".combined_file.csv", "r") as f:
            lines = f.readlines()

        lines = [line for line in lines if line.count(",") >= 4]
        with open(output_file_name, "w") as f:
            f.writelines(lines)
            print(f'Converted File saved as : {output_file_name}')

    Remove_InCompleted_requests()


def Grep_the_Stuffs_From_the_XML_History_log(file_name):
    # pass

    with open(file_name, "r") as file:
        for line in file.readlines():
            if "<request" in line:
                # print(line)
                with open(".request.xml", "a") as file:
                    take_req = False
                    file.writelines(line.replace('<request base64="true"><![CDATA[','').replace(']]></request>',','))
            
            if "response>" in line:
                with open(".response.xml", "a") as file:
                    take_req = False
                    file.writelines(line.replace('<response base64="true"><![CDATA[','').replace(']]></response>',','))
            
            if "method>" in line:

                with open(".method.xml", "a") as file:
                    take_req = False
                    file.writelines(line.replace('<method><![CDATA[','').replace(']]></method>',','))

            if "url>" in line:

                with open(".url.xml", "a") as file:
                    take_req = False
                    file.writelines(line.replace('<url><![CDATA[','').replace(',','%2c').replace(']]></url>',','))


def Empty_the_Temp_Files():

    file_list = [".method.xml", ".request.xml", ".response.xml",".url.xml",".combined_file.csv"]

    for file in file_list:
        if os.path.exists(file):
            try:
                os.remove(file)
            except:
                print(f"An error occurred while trying to remove {file}")
        else:
            pass


# IN ACTION

Empty_the_Temp_Files()

try:

    Grep_the_Stuffs_From_the_XML_History_log(sys.argv[1])
except:
    
    print('Example Usage: python3 2WStalker.py <Your history log file in the format of .xml>\n')


try:
    Convert_2_WStalker_CSV()
except:
    print(f"Something went wrong : Some special charectors in your {sys.argv[1]} may be screwing the script :/ \n")


Empty_the_Temp_Files()