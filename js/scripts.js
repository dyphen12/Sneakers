function initWorkbook() {

    var std = "http://127.0.0.1:5000/init/%";


    var workbooktitle = document.getElementById("init-wb-input").value;
    console.log(workbooktitle);

    var url = std.replace('%', workbooktitle);

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}

function expandWorkbook() {

    var std = "http://127.0.0.1:5000/expand/%";

    var workbooktitle = document.getElementById("init-wb-input").value;
    var expandsize = document.getElementById("new-wb-size").value;
    console.log(expandsize);
    console.log(workbooktitle);


     var query = '{"results": {"title": "%","size": $}}'

     var query2 = query.replace('%', workbooktitle);
     var finalquery = query2.replace('$', expandsize);

     var url = std.replace('%', finalquery)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

function imagingWorkbook() {

    var std = "http://127.0.0.1:5000/imaging/%";

    var query = '{"results": {"title": "%","from": #,"to": &}}'

    var workbooktitle = document.getElementById("init-wb-input").value;
    var dirfrom = document.getElementById("imaging-from").value;
    var dirto = document.getElementById("imaging-to").value;

    console.log(query);

    var query1 = query.replace('%', workbooktitle);
    var query2 = query1.replace('#', dirfrom);
    var query3 = query2.replace('&', dirto);

    var url = std.replace('%',query3)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

function syncWorkbook() {

    var std = "http://127.0.0.1:5000/sync/%";

    var workbooktitle = document.getElementById("init-wb-input").value;
    console.log(workbooktitle);

    var url = std.replace('%', workbooktitle);

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail');

      } else {
        console.log(res);
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;




    return true;
}

function sync2Workbook() {

    var workbooktitle = document.getElementById("init-wb-input").value;
    var acode = document.getElementById("send-code").value;

    var std = "http://127.0.0.1:5000/sync2/%";

     var query = '{"results": {"title": "%","code": $}}';

     var query2 = query.replace('%', workbooktitle);
     var finalquery = query2.replace('$', acode);

     var url = std.replace('%', finalquery)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

