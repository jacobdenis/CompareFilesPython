import os
import difflib,sys

config ='C:\\Users\\ACOB\Desktop\\PythonProject\\filehandling\\file1.txt'
config1 ='C:\\Users\\ACOB\Desktop\\PythonProject\\filehandling\\file2.txt'

with open(config,'r') as f1, open(config1,'r') as f2:
    #diff = difflib.ndiff(f1.readlines(),f2.readlines())    
    diff = difflib.unified_diff(f1.readlines(),f2.readlines())   
    html=f"""
    <!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>Changes Made Table</h2>         
  <table class="table table-bordered table-dark">
    <thead>
      <tr>
        <th>Last Record {config}</th>
        <th>Latest Record {config1}</th>
      </tr>
    </thead>
    <tbody>
 """
    count=0
    for line in diff:
         #sys.stdout.write(line)
       
        if line.startswith('-'):
            if count==0:
                html+="<tr>"
            html+="<td >{}</td>".format(line)
            count+=1
        else:
            html+="<td ></td>"
            count+=1
        if line.startswith('+'):
            if count==0:
                html+="<tr>"
            html+="<td >{}</td>".format(line)
            count+=1
        else:
            html+="<td></td>"
            count+=1
        if count==2:
            html+="</tr>"
            count=0
     
    html+="""
            </tbody>
  </table>
</div>

</body>
</html>
    """
file_ = open('result.html', 'w')
file_.write(html)
file_.close()