function initWorkbook() {

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/init/%";


    var workbooktitle = document.getElementById("init-wb-input").value;
    console.log(workbooktitle);

    document.getElementById("init-status").innerHTML = 'Loading Workbook...';

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
        document.getElementById("workbook-info").style.opacity = 10;
        infoWorkbook();
        document.getElementById("init-status").innerHTML = '';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}

function expandWorkbook() {

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/expand/%";

    document.getElementById("expansion-status").style.opacity = 10;
    document.getElementById("expansion-status").innerHTML = 'Expanding! Please wait until it finishes...';

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
        document.getElementById("expansion-status").innerHTML = 'Expansion Failed';

      } else {
        console.log('Sy');
        document.getElementById("expansion-status").innerHTML = 'Expanded Successfully';
        infoWorkbook();
      }

      }else{
      document.getElementById("expansion-status").innerHTML = 'Expanding! Please wait until it finishes...';}

    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

function imagingWorkbook() {

    document.getElementById("img-status").innerHTML = 'Inserting images... This could take minutes or several hours.';

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/imaging/%";

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
        infoWorkbook()
        document.getElementById("img-status").innerHTML = 'Images inserted successfully, sync and check your drive!';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

function drivecodeWorkbook() {

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/drive/%";

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
        document.getElementById("send-wb-aco").style.opacity = 10;
        document.getElementById("send-wb-aco").href = res;
        document.getElementById("send-wb-code").style.opacity = 10;
        document.getElementById("send-wb-button").style.opacity = 10;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;


}

function syncWorkbook() {

    document.getElementById("sync-result").innerHTML = 'Syncing...';

    var workbooktitle = document.getElementById("init-wb-input").value;
    var acode = document.getElementById("send-wb-code").value;

    document.getElementById("send-wb-aco").style.opacity = 0;
    document.getElementById("send-wb-aco").innerHTML = 'Please wait...';
    document.getElementById("send-wb-code").style.opacity = 0;
    document.getElementById("send-wb-button").style.opacity = 0;

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/sync/%";

    cryptedcode = acode.replace('/','totona')

     var query = '{"results": {"title": "%","code": "$"}}'



     var query2 = query.replace('%', workbooktitle);
     var finalquery = query2.replace('$', cryptedcode);

     var url = std.replace('%', finalquery)

     console.log(url)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
        infoWorkbook();
        document.getElementById("sync-result").innerHTML = 'Succesfully Synced! Check your drive!';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

function infoWorkbook() {

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/info/%";

    document.getElementById("workbook-info").style.opacity = 10;


    var workbooktitle = document.getElementById("init-wb-input").value;
    console.log(workbooktitle);

    var url = std.replace('%', workbooktitle);

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);
      console.log('Toy aqui pajuo');
      tit = res['composer']['title'];
      siz = res['composer']['size'];
      syn = res['composer']['synced'];
      docn = res['composer']['doc_name'];
      document.getElementById("wb-title").innerHTML = res['composer']['title'];
      document.getElementById("wb-size").innerHTML = siz;
      if (syn == true) {
      document.getElementById("wb-sync").innerHTML = 'Synced to Google Drive';}
      else{
      document.getElementById("wb-sync").innerHTML = 'Not Synced';
      }
      document.getElementById("wb-docname").innerHTML = docn;

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

function updateWorkbook() {

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/update/%";


    var workbooktitle = document.getElementById("init-wb-input").value;
    console.log(workbooktitle);

    document.getElementById("update-status").innerHTML = 'Updating prices...';

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
        document.getElementById("workbook-info").style.opacity = 10;
        infoWorkbook();
        document.getElementById("update-status").innerHTML = 'Workbook prices up to date!';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}

function updateDB() {

    var std = "http://sneakers-api-server.eba-ymfdhzi3.us-east-2.elasticbeanstalk.com/updatedb/%";


    var workbooktitle = document.getElementById("init-wb-input").value;
    console.log(workbooktitle);

    document.getElementById("updatedb-status").innerHTML = 'Updating all the sneakers...';

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
        document.getElementById("workbook-info").style.opacity = 10;
        infoWorkbook();
        document.getElementById("updatedb-status").innerHTML = 'Sneakers up to date!';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}


