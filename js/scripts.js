function initWorkbook() {

    var std = "https://sneakers-app-api.herokuapp.com/init/%";


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

    var std = "https://sneakers-app-api.herokuapp.com/expand/%";

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

    var std = "https://sneakers-app-api.herokuapp.com/imaging/%";

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

    var std = "https://sneakers-app-api.herokuapp.com/drive/%";

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

    var std = "https://sneakers-app-api.herokuapp.com/sync/%";

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

    var std = "https://sneakers-app-api.herokuapp.com/info/%";

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

    var std = "https://sneakers-app-api.herokuapp.com/update/%";


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

    var std = "https://sneakers-app-api.herokuapp.com/updatedb/%";


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


// Airtable's functions

function initTable() {

    var std = "https://sneakers-app-api.herokuapp.com/inittable/%";


    var workbooktitle = document.getElementById("init-wb-input").value;
    console.log(workbooktitle);

    document.getElementById("init-status").innerHTML = 'Loading Table...';

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
        infoTable();
        document.getElementById("init-status").innerHTML = '';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}

function infoTable() {

    var std = "https://sneakers-app-api.herokuapp.com/infotable/%";

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
      document.getElementById("wb-sync").innerHTML = 'Synced to Airtable';}
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


function deployTable() {

    var std = "https://sneakers-app-api.herokuapp.com/deploytable/%";

    document.getElementById("expansion-status").style.opacity = 10;
    document.getElementById("expansion-status").innerHTML = 'Deploying! Please wait until it finishes...';

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
        document.getElementById("expansion-status").innerHTML = 'Deploy Failed';

      } else {
        console.log('Sy');
        document.getElementById("expansion-status").innerHTML = res;
        infoTable();
      }

      }else{
      document.getElementById("expansion-status").innerHTML = 'Deploying! Please wait until it finishes...';}

    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

function updateTable() {

    var std = "https://sneakers-app-api.herokuapp.com/updatetable/%";


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
        infoTable();
        document.getElementById("update-status").innerHTML = 'Table prices up to date!';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}

function apiVersion() {

    var std = "https://sneakers-app-api.herokuapp.com/";


    document.getElementById("version").innerHTML = 'Loading...';

    var url = std

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
        document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}


// --------- STOCKDOTSHOP ----------

// These are the functions of the main Stockdotshop app
// Status: Under Development
// Note: Fixes for organization a better standard resourcing of functions


// ########## INDEX MAIN PROCESSES ########

function getUsername(ssid) {

    var std = "https://sneakers-app-api.herokuapp.com/user/%";


    var url = std.replace('%', ssid);

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

        document.getElementById("user-welcome").innerHTML = 'Welcome, ' + res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}

function sneakerData() {

    document.getElementById("sneaker-container").innerHTML = 'Loading...';



    apiVersion();

    // var std = "http://127.0.0.1:5000/alldata";

    var std = "https://sneakers-app-api.herokuapp.com/alldataindex/%";

    var sneakerLivePage = document.getElementById("sneaker-quantity").value;


    var url = std.replace('%', sneakerLivePage);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        var sneakerLiveAmount = document.getElementById("sneaker-quantity").value;

      document.getElementById("sneakers-live-amount").innerHTML = sneakerLiveAmount;
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      // console.log(res);


      document.getElementById("sneaker-container").style.opacity = "0.0";
      asyncCall(res);

      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
        // document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;

}

function resolveAfter2Seconds(res) {
  return new Promise(resolve => {
    setTimeout(() => {
       console.log(res)

       var shoecard = document.getElementById('shoe-card');
       console.log(shoecard);

        var sneakerLiveAmount = document.getElementById("sneaker-quantity").value;

        var counter = 0;

        console.log(counter)


        document.getElementById("sneaker-container").innerHTML = '';

        for (sneaker in res) {

          console.log(`${sneaker}: ${res[sneaker]}`);
          //console.log(sneaker)


          var snk = res[sneaker];

          //console.log(snk['name'])

          // console.log(snk[prop]);
          // console.log(`${prop}: ${snk[prop]}`);

          // Object Creation

          //Big Card
          var card = document.createElement("div");

          card.className = "mdl-cell mdl-cell--3-col mdl-cell--4-col-tablet mdl-cell--4-col-phone mdl-card mdl-shadow--3dp";

          // Four childs

          // Child 1 - Img

          var cardimg = document.createElement("div");

          cardimg.className = "mdl-card__media";

          var img = document.createElement('img');
          img.src = snk['thumbnail'];

          cardimg.appendChild(img);

          // Child 2 - Title

          var cardtitle = document.createElement("div");

          cardtitle.id = snk['id'];

          cardtitle.className = "mdl-card__title";

          var title = document.createElement("h4");

          title.innerHTML = snk['name'];

          console.log(snk)

          title.className = "mdl-card__title-text"

          cardtitle.appendChild(title)

          // Child 3 - Supporting Text

          var cardsubtext = document.createElement("div");

          cardsubtext.className = "mdl-card__supporting-text";

          var subtext = document.createElement("span");


          subtext.innerHTML = snk['colorway'] + "<br><br>";

          subtext.className = "mdl-typography--font-light mdl-typography--subhead"

          var subtextprice = document.createElement("span");

          subtextprice.innerHTML = snk['NZDvalue'] + "$";

          subtextprice.className = "mdl-typography--font-light mdl-typography--subhead"

          cardsubtext.appendChild(subtext)
          cardsubtext.appendChild(subtextprice)

          // Child 4 - Button

          var cardaction = document.createElement("div");

          cardaction.className = "mdl-card__actions";

          var linktoaction = document.createElement("a");

          linktoaction.href = snk['link3'];

          linktoaction.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktoaction.innerHTML = 'See';

          var icon = document.createElement("i");

          icon.className = "material-icons";

          icon.innerHTML = "chevron_right"

          linktoaction.appendChild(icon)
          cardaction.appendChild(linktoaction)

          // Child 5 Fav button

          var linktofav = document.createElement("a");

          linktofav.id = snk['sku'];

          // linktofav.href = snk['link3'];

          linktofav.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktofav.innerHTML = 'Save ';

          linktofav.onclick = function() {saveSneakerLite(this.id);}

          var ficon = document.createElement("i");

          //var skid = snk['USDvalue'];

          //ficon.id = skid;

          ficon.className = "material-icons";

          ficon.innerHTML = "favorite_border"


          linktofav.appendChild(ficon)
          cardaction.appendChild(linktofav)



          // Append Childs to Mother

          card.appendChild(cardimg)
          card.appendChild(cardtitle)
          card.appendChild(cardsubtext)
          card.appendChild(cardaction)

          // Append to Sneaker Container

          var sneakercontainer = document.getElementById('sneaker-container');

          sneakercontainer.appendChild(card)

          counter++;

          console.log(counter)

          // checkSneakers(skid);

          if (counter == sneakerLiveAmount) {

          console.log('Hooray!')

          break;

          }


          // console.log(card)


        }



      resolve('resolved');
    }, 2);
  });
}

async function asyncCall(res) {
  console.log('calling');
  const result = await resolveAfter2Seconds(res);
  console.log(result);
  console.log('Here I should Fav everything but I dont know how :(');
  loadsneakerlite();


  // expected output: "resolved"
}


function loadHome() {

  // RYZEN: First (R1)
  console.log('R1 Started')

  // This deletes some item that bothers.


  // Loads Sneaker Live Table Routine


  // Start SSID
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {

  // R1 Fail end
    //document.getElementById("mySidebar").innerHTML = '';
    //document.getElementById("pageC").innerHTML = 'Please Login';
    console.log('Please Login')
    HomeData();

  }
  else {

    makelogin();

    // RYZEN: Second (R2)
    console.log('R2 Started')

    // First Message to Console

    console.log(ssid);
    console.log('Somos los que somos');

    // User's name routines

    // Get user name from index.html (this is a faulty one) needs to be in a future onload for index only.
    getUsername(ssid);
    sneakerData();



  }

}

function loadHomeLite() {

  // RYZEN: First (R1)
  console.log('R1 Started')

  // This deletes some item that bothers.


  // Loads Sneaker Live Table Routine


  // Start SSID
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {

  // R1 Fail end
    //document.getElementById("mySidebar").innerHTML = '';
    //document.getElementById("pageC").innerHTML = 'Please Login';
    console.log('Please Login')
    HomeData();

  }
  else {

    // RYZEN: Second (R2)
    console.log('R2 Started')

    // First Message to Console

    console.log(ssid);
    console.log('Somos los que somos');

    // User's name routines

    // Get user name from index.html (this is a faulty one) needs to be in a future onload for index only.
    sneakerData();



  }

}

function HomeData() {

    document.getElementById("sneaker-container").innerHTML = 'Loading...';

    apiVersion();

    // var std = "http://127.0.0.1:5000/alldata";

    var std = "https://sneakers-app-api.herokuapp.com/alldataindex/%";

    var sneakerLivePage = document.getElementById("sneaker-quantity").value;


    var url = std.replace('%', sneakerLivePage);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        var sneakerLiveAmount = document.getElementById("sneaker-quantity").value;

      document.getElementById("sneakers-live-amount").innerHTML = sneakerLiveAmount;
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      // console.log(res);



      HomeDataasyncCall(res);

      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
        // document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;

}

function HomeDataResolve(res) {
  return new Promise(resolve => {
    setTimeout(() => {
       //console.log(res)

       var shoecard = document.getElementById('shoe-card');
       console.log(shoecard);

        var sneakerLiveAmount = document.getElementById("sneaker-quantity").value;

        var counter = 0;

        document.getElementById("sneaker-container").style.opacity = "0.0";
        document.getElementById("sneaker-container").innerHTML = '';

        for (sneaker in res) {

          //console.log(`${sneaker}: ${res[sneaker]}`);
          //console.log(sneaker)


          var snk = res[sneaker];

          //console.log(snk['name'])

          // console.log(snk[prop]);
          // console.log(`${prop}: ${snk[prop]}`);

          // Object Creation

          //Big Card
          var card = document.createElement("div");

          card.className = "mdl-cell mdl-cell--3-col mdl-cell--4-col-tablet mdl-cell--4-col-phone mdl-card mdl-shadow--3dp";

          // Four childs

          // Child 1 - Img

          var cardimg = document.createElement("div");

          cardimg.className = "mdl-card__media";

          var img = document.createElement('img');
          img.src = snk['thumbnail'];

          cardimg.appendChild(img);

          // Child 2 - Title

          var cardtitle = document.createElement("div");

          cardtitle.id = snk['id'];

          cardtitle.className = "mdl-card__title";

          var title = document.createElement("h4");

          title.innerHTML = snk['name'];

          console.log(snk)

          title.className = "mdl-card__title-text"

          cardtitle.appendChild(title)

          // Child 3 - Supporting Text

          var cardsubtext = document.createElement("div");

          cardsubtext.className = "mdl-card__supporting-text";

          var subtext = document.createElement("span");


          subtext.innerHTML = snk['colorway'] + "<br><br>";

          subtext.className = "mdl-typography--font-light mdl-typography--subhead"

          var subtextprice = document.createElement("span");

          subtextprice.innerHTML = snk['NZDvalue'] + "$";

          subtextprice.className = "mdl-typography--font-light mdl-typography--subhead"

          cardsubtext.appendChild(subtext)
          cardsubtext.appendChild(subtextprice)

          // Child 4 - Button

          var cardaction = document.createElement("div");

          cardaction.className = "mdl-card__actions";

          var linktoaction = document.createElement("a");

          linktoaction.href = snk['link3'];

          linktoaction.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktoaction.innerHTML = 'See';

          var icon = document.createElement("i");

          icon.className = "material-icons";

          icon.innerHTML = "chevron_right"

          linktoaction.appendChild(icon)
          cardaction.appendChild(linktoaction)

          // Child 5 Fav button

          var linktofav = document.createElement("a");

          linktofav.id = snk['sku'];

          // linktofav.href = snk['link3'];

          linktofav.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktofav.innerHTML = 'Save ';

          linktofav.onclick = function() {togglelogin();}

          var ficon = document.createElement("i");

          //var skid = snk['USDvalue'];

          //ficon.id = skid;

          ficon.className = "material-icons";

          ficon.innerHTML = "favorite_border"


          linktofav.appendChild(ficon)
          cardaction.appendChild(linktofav)



          // Append Childs to Mother

          card.appendChild(cardimg)
          card.appendChild(cardtitle)
          card.appendChild(cardsubtext)
          card.appendChild(cardaction)

          // Append to Sneaker Container

          var sneakercontainer = document.getElementById('sneaker-container');

          sneakercontainer.appendChild(card)

          counter++;

          console.log(counter)

          // checkSneakers(skid);

          if (counter == sneakerLiveAmount) {

          console.log('Hooray!')

          break;

          }


          // console.log(card)


        }



      resolve('resolved');
    }, 2);
  });
}

async function HomeDataasyncCall(res) {
  console.log('calling');
  const result = await HomeDataResolve(res);
  console.log(result);
  document.getElementById("sneaker-container").style.opacity = "1.0";

  // expected output: "resolved"
}



// -------- LOGIN - SIGN UP ----------

// Notes: There's no sign up process yet

// Front: Called on Index
function login() {

    var x , y;

    // Get the value of the input field with id="numb"
    x = document.getElementById("login-mail").value;
    y = document.getElementById("loginpass").value;

    var token = "user=%&pass=$"
    var credentialx = token.replace('%',x);
    var credential = credentialx.replace('$',y);


    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        // document.getElementById("demo").innerHTML = 'Wrong password or username';

      } else {
        // document.getElementById("demo").innerHTML = 'Succesfully Logged in';
        var cookiephrase = 'ssid=';
        var ssidcookie = cookiephrase + res;
        sessionStorage.setItem('ssid',res);
        var andnavcontainer = document.getElementById('nav-cont');

        andnavcontainer.innerHTML = '';

        makelogin();
        location.reload();
      }

      }
    };
    xhttp.open("POST", "https://sneakers-app-api.herokuapp.com/auth", true);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send(credential);

}

// Back Processes
function setCookie(key, value) {
            var expires = new Date();
            expires.setTime(expires.getTime() + (1 * 24 * 60 * 60 * 1000));
            document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
        }

// Called on: login()>makelogin() / R2 /
// Just changes the Header to an Logged Header
function makeloginProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

    var drawSignin = document.getElementById('draw-signin').innerHTML = 'My Sneakers';
    var drawLogin = document.getElementById('draw-login').style.display = 'none';
    document.getElementById('more-button').style.display = 'inline';

    document.getElementById('draw-signin').onclick = dummy;


    //Nav Container
          var navcontainer = document.createElement("nav");

          navcontainer.className = "android-navigation mdl-navigation";

          // Four childs

          // Child 1 - a

          var aname = document.createElement("a");

          aname.className = "mdl-navigation__link mdl-typography--text-uppercase";

          aname.innerHTML = 'Welcome, ';

          aname.id = 'user-welcome';

          navcontainer.appendChild(aname);

       // document.getElementById('loginbots').style.display = "inline";


       var andnavcontainer = document.getElementById('nav-cont');

          andnavcontainer.appendChild(navcontainer)

      resolve('makeloginProcess() ended');
    }, 0);
  });
}

// Called on: Login
async function makelogin() {

  console.log('calling');
  const result = await makeloginProcess();
  console.log(result);
  document.getElementById('loginbots').style.display = 'none';
  loaduser();


  // expected output: "resolved"
}

// Front Ad hoc

function toggleloginProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        document.getElementById('loginbots').style.display = "inline";

      resolve('resolved');
    }, 2);
  });
}

async function togglelogin() {
  console.log('calling');
  const result = await toggleloginProcess();
  console.log(result);
  // expected output: "resolved"
}

function togglesignupProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        document.getElementById('saininbots').style.display = "inline";

      resolve('resolved');
    }, 2);
  });
}

async function togglesignup() {
  console.log('calling');
  const result = await togglesignupProcess();
  console.log(result);
  // expected output: "resolved"
}

function gosignupProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        document.getElementById('formasignup').innerHTML = 'Loading...';



      resolve('resolved');
    }, 2);
  });
}

async function gosignup() {
  console.log('calling');
  const result = await gosignupProcess();
  console.log(result);
  // expected output: "resolved"
}



// ########## USER APP MAIN PROCESSES ########


// Just a Logout

function logout() {
  sessionStorage.removeItem('ssid');
  window.location.href = "index.html";

}


function logoutlite() {
  sessionStorage.removeItem('ssid');
}

// COOKIES

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
                    }
          if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
                    }
                  }
                  return "";
}


// Loads Username for the user.html page
// STARTED BY:

// loaduser():
function getUsernameprofile(ssid) {

    var std = "https://sneakers-app-api.herokuapp.com/user/%";


    var url = std.replace('%', ssid);

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

        document.getElementById("hello-user").innerHTML = 'Hello, ' + res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}


// --------- USER DATA ----------

// RYZEN: Onload Call

function loaduser() {


  // RYZEN: First (R1)
  console.log('R1 Started')

  // This deletes some item that bothers.
  document.getElementById('more-button').style.display = 'none';
  var andnavcontainer = document.getElementById('nav-cont');
  andnavcontainer.innerHTML = '';


  // Start SSID
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {

  // R1 Fail end
    document.getElementById("hello-user").innerHTML = 'Please Login';
    document.getElementById("stockdotshop-content").innerHTML = '';
    document.getElementById("sneaker-user").innerHTML = '';
    document.getElementById("sneaker-live").innerHTML = '';
    console.log('Please Login')

  }
  else {


    // RYZEN: Second (R2)
    console.log('R2 Started')


    // First Message to Console

    console.log(ssid);
    console.log('Somos los que somos');


    // User's name routines


    // Get user name from index.html (this is a faulty one) needs to be in a future onload for index only.
    getUsername(ssid);

    // Get user name for user.html (this is the main one for the profile so thats why)
    // So it only changes the "Hello, user"
    getUsernameprofile(ssid);



    // Does the header changing for user.html
    makeloginProcess();
    document.getElementById('more-button').style.display = 'inline';


    //RYZEN: Third (R3)
    //Loads My Sneaker Table Routine
    userData(ssid);



    //var usernurl = 'http://detfladder.pythonanywhere.com/usern/' + ssid;
    //fetch(usernurl)
    //.then(response => response.json())
    //.then(data => document.getElementById("username").innerHTML = data);

  }

}

// ---- MY SNEAKER TABLE ROUTINE --------

//--------- User Data -------------------

function userData(ssid) {

    document.getElementById("sneaker-container-user").innerHTML = 'Loading...';

    apiVersion();


    var std = "https://sneakers-app-api.herokuapp.com/userdata/%";


    var url = std.replace('%', ssid);


    // document.getElementById("version").innerHTML = 'Loading...';

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      // console.log(res);




      if (res == 'fail'){
        document.getElementById("sneaker-container-user").innerHTML = 'Nothing to show here, try searching your favorite sneakers or you can explore all the database.';
        console.log('Fail')

      } else {
        console.log('Sy')
        userdataCall(res);
        // document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;

}

function userdataProcess(res) {
  return new Promise(resolve => {
    setTimeout(() => {
       console.log(res)

       // My Sneaker Table Card Creator
       // res = json table
       // skid = snk['name']



       //Card Creation
       var shoecard = document.getElementById('shoe-card');
       console.log(shoecard);



        //console.log(counter)

        document.getElementById("sneaker-container-user").innerHTML = '';

        //

        for (sneaker in res) {

          console.log(`${sneaker}: ${res[sneaker]}`);
          //console.log(sneaker)


          var snk = res[sneaker];

          //console.log(snk['name'])

          // console.log(snk[prop]);
          // console.log(`${prop}: ${snk[prop]}`);

          // Object Creation

          //Big Card
          var card = document.createElement("div");

          card.className = "mdl-cell mdl-cell--3-col mdl-cell--4-col-tablet mdl-cell--4-col-phone mdl-card mdl-shadow--3dp";

          // Four childs

          // Child 1 - Img

          var cardimg = document.createElement("div");

          cardimg.className = "mdl-card__media";

          var img = document.createElement('img');
          img.src = snk['thumbnail'];

          cardimg.appendChild(img);

          // Child 2 - Title

          var cardtitle = document.createElement("div");

          cardtitle.id = snk['id'];

          cardtitle.className = "mdl-card__title";

          var title = document.createElement("h4");

          title.innerHTML = snk['name'];

          console.log(snk)

          title.className = "mdl-card__title-text"

          cardtitle.appendChild(title)

          // Child 3 - Supporting Text

          var cardsubtext = document.createElement("div");

          cardsubtext.className = "mdl-card__supporting-text";

          var subtext = document.createElement("span");


          subtext.innerHTML = snk['colorway'] + "<br><br>";

          subtext.className = "mdl-typography--font-light mdl-typography--subhead"

          var subtextprice = document.createElement("span");

          subtextprice.innerHTML = snk['NZDvalue'] + "$";

          subtextprice.className = "mdl-typography--font-light mdl-typography--subhead"

          cardsubtext.appendChild(subtext)
          cardsubtext.appendChild(subtextprice)

          // Child 4 - Button

          var cardaction = document.createElement("div");

          cardaction.className = "mdl-card__actions";

          var linktoaction = document.createElement("a");

          linktoaction.href = snk['link3'];

          linktoaction.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktoaction.innerHTML = 'See';

          var icon = document.createElement("i");

          icon.className = "material-icons";

          icon.innerHTML = "chevron_right"

          linktoaction.appendChild(icon)
          cardaction.appendChild(linktoaction)

          // Child 5 Fav button

          var linktofav = document.createElement("a");

          linktofav.id = snk['sku'];

          // linktofav.href = snk['link3'];

          linktofav.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktofav.innerHTML = 'Save ';


          // Adds the saveSneaker() function to the card onclick.

          linktofav.onclick = function() {saveSneakerLite(this.id);}

          var ficon = document.createElement("i");

          var skid = snk['name'];

          ficon.id = skid;

          ficon.className = "material-icons";

          ficon.innerHTML = "favorite_border"

          linktofav.appendChild(ficon)
          cardaction.appendChild(linktofav)



          // Append Childs to Mother

          card.appendChild(cardimg)
          card.appendChild(cardtitle)
          card.appendChild(cardsubtext)
          card.appendChild(cardaction)

          // Append to Sneaker Container

          var sneakercontainer = document.getElementById('sneaker-container-user');

          sneakercontainer.appendChild(card)

          markSneakerFav(snk['sku']);


          // Ryzen Fourth (R4)
          // RYZEN SUBROUTINE I (R3 Call): Sneaker Checker
          // checkSneakers(skid);

          // console.log(card)

        }

      resolve('resolved');
    }, 2);
  });
}

async function userdataCall(res) {
  console.log('calling');
  const result = await userdataProcess(res);
  console.log(result);

  // expected output: "resolved"
}


//// RYZEN SUBROUTINE I: Mark Sneakers Faved

function markSneakerFav(ide){

        console.log('This is already faved ewe')
        //targetDiv.textContent = "favorite";

        sss = '[id="%"]';
        query = sss.replace('%', ide)

        var elements = document.querySelectorAll(query);

        for(var i = 0; i < elements.length; i++) {
            var icon = elements[i].getElementsByClassName("material-icons")[0];
            icon.innerHTML = 'favorite';
        }



}


//--------- SNEAKERS CARD ONCLICK FUNCTIONS -----------

function dummy() {

  console.log('I love you!');
  window.location.replace("user.html")

}

//----------- SAVE ----------


async function saveSneakerLite(ide) {
  console.log('fav');

  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {
    //document.getElementById("mySidebar").innerHTML = '';
    //document.getElementById("pageC").innerHTML = 'Please Login';
    console.log('Ando buscando la chica que este mas buena')






  }
  else {
    console.log(ssid);
    console.log('this the fav icon uwu');




    var targetDiv = document.getElementById(ide).getElementsByClassName("material-icons")[0];
    var option = targetDiv.textContent;

    console.log(option)

    if (option == 'favorite_border') {

        console.log('This is going to be a fav uwu')
        sneakerSender(ssid, ide);
        //loaduserUpdate();
        //targetDiv.textContent = "favorite";

        sss = '[id="%"]';
        query = sss.replace('%', ide)

        var elements = document.querySelectorAll(query);

        for(var i = 0; i < elements.length; i++) {
            var icon = elements[i].getElementsByClassName("material-icons")[0];
            icon.innerHTML = 'favorite';
        }

    } else {

        console.log('owo you dont like it anymore?')
        sneakerUnfaver(ssid, ide)
        // await new Promise(r => setTimeout(r, 2000));
        //loaduserUpdate();

        //targetDiv.textContent = "favorite_border";

        sss = '[id="%"]';
        query = sss.replace('%', ide)

        var elements = document.querySelectorAll(query);

        for(var i = 0; i < elements.length; i++) {
            var icon = elements[i].getElementsByClassName("material-icons")[0];
            icon.innerHTML = 'favorite_border';
        }


    }



    // targetDiv.onclick = function() {unfavSneaker(this.id);}




    console.log('fav ended awa');

    //sneakerSender(ssid, ide);


    //document.getElementById('more-button').style.display = 'inline';


    //var usernurl = 'http://detfladder.pythonanywhere.com/usern/' + ssid;
    //fetch(usernurl)
    //.then(response => response.json())
    //.then(data => document.getElementById("username").innerHTML = data);

  }




  const result = await saveSneakerProcess();
  console.log(ide);
  // expected output: "resolved"
}


async function saveSneaker(ide) {
  console.log('fav');

  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {
    //document.getElementById("mySidebar").innerHTML = '';
    //document.getElementById("pageC").innerHTML = 'Please Login';
    console.log('Ando buscando la chica que este mas buena')






  }
  else {
    console.log(ssid);
    console.log('this the fav icon uwu');




    var targetDiv = document.getElementById(ide).getElementsByClassName("material-icons")[0];
    var option = targetDiv.textContent;

    console.log(option)

    if (option == 'favorite_border') {

        console.log('This is going to be a fav uwu')
        sneakerSender(ssid, ide);
        loaduserUpdate();
        //targetDiv.textContent = "favorite";

        sss = '[id="%"]';
        query = sss.replace('%', ide)

        var elements = document.querySelectorAll(query);

        for(var i = 0; i < elements.length; i++) {
            var icon = elements[i].getElementsByClassName("material-icons")[0];
            icon.innerHTML = 'favorite';
        }

    } else {

        console.log('owo you dont like it anymore?')
        sneakerUnfaver(ssid, ide)
        // await new Promise(r => setTimeout(r, 2000));
        loaduserUpdate();

        //targetDiv.textContent = "favorite_border";

        sss = '[id="%"]';
        query = sss.replace('%', ide)

        var elements = document.querySelectorAll(query);

        for(var i = 0; i < elements.length; i++) {
            var icon = elements[i].getElementsByClassName("material-icons")[0];
            icon.innerHTML = 'favorite_border';
        }


    }



    // targetDiv.onclick = function() {unfavSneaker(this.id);}




    console.log('fav ended awa');

    //sneakerSender(ssid, ide);


    //document.getElementById('more-button').style.display = 'inline';


    //var usernurl = 'http://detfladder.pythonanywhere.com/usern/' + ssid;
    //fetch(usernurl)
    //.then(response => response.json())
    //.then(data => document.getElementById("username").innerHTML = data);

  }




  const result = await saveSneakerProcess();
  console.log(ide);
  // expected output: "resolved"
}

function saveSneakerProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        // document.getElementById('loginbots').style.display = "inline";
       console.log('Saved!')
      resolve('resolved');
    }, 2);
  });
}

function sneakerSender(ssid, sku) {

    var std = "https://sneakers-app-api.herokuapp.com/savethis/%";

    console.log(ssid);
    console.log(sku);


     var query = '{"results": {"ssid": "%","sku": "$"}}'

     var query2 = query.replace('%', ssid);
     var finalquery = query2.replace('$', sku);

     var url = std.replace('%', finalquery)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')
      } else {
        console.log('Sy');

      }

      }else{
      console.log('Kwait')}

    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

//----------- UNSAVE ----------


function unfavSneakerProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        // document.getElementById('loginbots').style.display = "inline";
       console.log('Saved!')
      resolve('resolved');
    }, 2);
  });
}

function sneakerUnfaver(ssid, sku) {

    var std = "https://sneakers-app-api.herokuapp.com/deletethis/%";


     var query = '{"results": {"ssid": "%","sku": "$"}}'

     var query2 = query.replace('%', ssid);
     var finalquery = query2.replace('$', sku);

     var url = std.replace('%', finalquery)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')
      } else {
        console.log('Sy');

      }

      }else{
      console.log('Kwait')}

    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}


// --------- Profile Sneaker LIVE Fav already faved Routine-----------

function loadusersearchlite() {
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {
    console.log('And now I do and I am going to fav everything uwu')

  }
  else {

    usersearchDataLite(ssid);

  }

}

function usersearchDataLite(ssid) {

    var std = "https://sneakers-app-api.herokuapp.com/userdata/%";
    var url = std.replace('%', ssid);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      // console.log(res);

      usersearchCallLite(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
        // document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;

}

function usersearchProcessLite(res) {
  return new Promise(resolve => {
    setTimeout(() => {
       console.log(res)

        for (sneaker in res) {

          console.log(`${sneaker}: ${res[sneaker]}`);

          var snk = res[sneaker];

          markSneakerFav(snk['sku']);
        }
      resolve('resolved');
    }, 2);
  });
}

async function usersearchCallLite(res) {
  console.log('doing my jobbbb just faving everything here u know owo');
  const result = await usersearchProcessLite(res);
  console.log(result);
  document.getElementById("sneaker-container-search").style.opacity = "1.0";
  // expected output: "resolved"
}







function loaduserlite() {
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {
    console.log('And now I do and I am going to fav everything uwu')

  }
  else {
    userDataLite(ssid);

  }

}

function userDataLite(ssid) {

    var std = "https://sneakers-app-api.herokuapp.com/userdata/%";
    var url = std.replace('%', ssid);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      // console.log(res);

      userdataCallLite(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
        // document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;

}

function userdataProcessLite(res) {
  return new Promise(resolve => {
    setTimeout(() => {
       console.log(res)

        for (sneaker in res) {

          console.log(`${sneaker}: ${res[sneaker]}`);

          var snk = res[sneaker];

          markSneakerFav(snk['sku']);
        }
      resolve('resolved');
    }, 2);
  });
}

async function userdataCallLite(res) {
  console.log('doing my jobbbb just faving everything here u know owo');
  const result = await userdataProcessLite(res);
  console.log(result);
  document.getElementById("sneaker-container").style.opacity = "1.0";
  // expected output: "resolved"
}











function loadsneakerlite() {
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {
    console.log('And now I do and I am going to fav everything uwu')

  }
  else {
    sneakerDataLite(ssid);

  }

}

function sneakerDataLite(ssid) {

    var std = "https://sneakers-app-api.herokuapp.com/userdata/%";
    var url = std.replace('%', ssid);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      // console.log(res);

      sneakerdataCallLite(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
        // document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;

}

function sneakerdataProcessLite(res) {
  return new Promise(resolve => {
    setTimeout(() => {
       console.log(res)

        for (sneaker in res) {

          console.log(`${sneaker}: ${res[sneaker]}`);

          var snk = res[sneaker];

          markSneakerFav(snk['sku']);
        }
      resolve('resolved');
    }, 2);
  });
}

async function sneakerdataCallLite(res) {
  console.log('doing my jobbbb just faving everything here u know owo');
  const result = await userdataProcessLite(res);
  console.log(result);
  document.getElementById("sneaker-container").style.opacity = "1.0";
  // expected output: "resolved"
}

//#########################

function loaduserUpdate() {
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {
    console.log('And now I do and I am going to fav everything uwu')
  }
  else {
    userData(ssid);

  }

}


// Sign Up Process

function SignUpNow() {

    document.getElementById("signup-status").innerHTML = 'Signing up...';

    var std = "https://sneakers-app-api.herokuapp.com/signup/%";

    var query = '{"results": {"name": "%","lastname": "#","email": "&","password": "$"}}'

    var signname = document.getElementById("name").value;
    var signlastname = document.getElementById("lastname").value;
    var signemail = document.getElementById("email").value;
    var signpassword = document.getElementById("signpassword").value;

    console.log(query);

    var query1 = query.replace('%', signname);
    var query2 = query1.replace('#', signlastname);
    var query3 = query2.replace('&', signemail);
    var query4 = query3.replace('$', signpassword);

    if (signname == '' || signlastname == '' || signemail == '' || signpassword == '' ) {

        document.getElementById("signup-status").innerHTML = 'Fill the entire form';
        return true



    }

    var url = std.replace('%',query4)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);



      if (res == 'User Already Registered'){
        console.log(res)




      } else {

      document.getElementById("signup-status").innerHTML = 'Eureka!';

        var cookiephrase = 'ssid=';

        var ssidcookie = cookiephrase + res;

        sessionStorage.setItem('ssid',res);

        location.href='user.html';

        console.log(res)



        // document.getElementById("img-status").innerHTML = 'Images inserted successfully, sync and check your drive!';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}


// SEARCH IMPLEMENTATION

function loadSearch() {


  // RYZEN: First (R1)
  console.log('R1 Started')



  // This deletes some item that bothers.
  document.getElementById('more-button').style.display = 'none';
  var andnavcontainer = document.getElementById('nav-cont');
  andnavcontainer.innerHTML = '';


  // Start SSID
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {

  // R1 Fail end
    //document.getElementById("hello-user").innerHTML = 'Please Login';
    //document.getElementById("stockdotshop-content").innerHTML = '';
    //document.getElementById("sneaker-user").innerHTML = '';
    //document.getElementById("sneaker-live").innerHTML = '';
    console.log('Please Login')
    document.getElementById("stockdotshop-content").innerHTML = 'Please Login';
    document.getElementById("sneaker-container-search").innerHTML = '';
    document.getElementById("sneaker-search").innerHTML = '';

  }
  else {


    // RYZEN: Second (R2)
    console.log('R2 Started')

    document.getElementById("sneaker-container-search").innerHTML = 'Search something first.';


    // First Message to Console

    console.log(ssid);
    console.log('Somos los que somos');


    // User's name routines


    // Get user name from index.html (this is a faulty one) needs to be in a future onload for index only.


    // Get user name for user.html (this is the main one for the profile so thats why)
    // So it only changes the "Hello, user"



    // Does the header changing for user.html
    makeloginProcess();
    document.getElementById('more-button').style.display = 'inline';

    getUsername(ssid);



    //var usernurl = 'http://detfladder.pythonanywhere.com/usern/' + ssid;
    //fetch(usernurl)
    //.then(response => response.json())
    //.then(data => document.getElementById("username").innerHTML = data);

  }

}

function searchData() {

    var searchquery = document.getElementById("search-query").value;


    console.log(searchquery)

    document.getElementById("sneaker-container-search").innerHTML = 'Loading...';

    apiVersion();


    var std = "https://sneakers-app-api.herokuapp.com/search/%";


    var url = std.replace('%', searchquery);


    // document.getElementById("version").innerHTML = 'Loading...';

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      // console.log(res);




      if (res == 'fail'){
        console.log('Fail')
        document.getElementById("sneaker-container-search").innerHTML = 'Nothing found :(. Try Some different keywords instead.';

      } else {
        document.getElementById("sneaker-container-search").style.opacity = "0.0";
        searchdataCall(res);
        loadusersearchlite();
        console.log('Sy')
        // document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;


}

function searchdataProcess(res) {
  return new Promise(resolve => {
    setTimeout(() => {
       console.log(res)

       // My Sneaker Table Card Creator
       // res = json table
       // skid = snk['name']



       //Card Creation
       var shoecard = document.getElementById('shoe-card');
       console.log(shoecard);



        //console.log(counter)

        document.getElementById("sneaker-container-search").innerHTML = '';




        //

        for (sneaker in res) {

          console.log(`${sneaker}: ${res[sneaker]}`);
          //console.log(sneaker)


          var snk = res[sneaker];

          //console.log(snk['name'])

          // console.log(snk[prop]);
          // console.log(`${prop}: ${snk[prop]}`);

          // Object Creation

          //Big Card
          var card = document.createElement("div");

          card.className = "mdl-cell mdl-cell--3-col mdl-cell--4-col-tablet mdl-cell--4-col-phone mdl-card mdl-shadow--3dp";

          // Four childs

          // Child 1 - Img

          var cardimg = document.createElement("div");

          cardimg.className = "mdl-card__media";

          var img = document.createElement('img');
          img.src = snk['thumbnail'];

          cardimg.appendChild(img);

          // Child 2 - Title

          var cardtitle = document.createElement("div");

          cardtitle.id = snk['id'];

          cardtitle.className = "mdl-card__title";

          var title = document.createElement("h4");

          title.innerHTML = snk['name'];

          console.log(snk)

          title.className = "mdl-card__title-text"

          cardtitle.appendChild(title)

          // Child 3 - Supporting Text

          var cardsubtext = document.createElement("div");

          cardsubtext.className = "mdl-card__supporting-text";

          var subtext = document.createElement("span");


          subtext.innerHTML = snk['colorway'] + "<br><br>";

          subtext.className = "mdl-typography--font-light mdl-typography--subhead"

          var subtextprice = document.createElement("span");

          subtextprice.innerHTML = snk['NZDvalue'] + "$";

          subtextprice.className = "mdl-typography--font-light mdl-typography--subhead"

          cardsubtext.appendChild(subtext)
          cardsubtext.appendChild(subtextprice)

          // Child 4 - Button

          var cardaction = document.createElement("div");

          cardaction.className = "mdl-card__actions";

          var linktoaction = document.createElement("a");

          linktoaction.href = snk['link3'];

          linktoaction.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktoaction.innerHTML = 'See';

          var icon = document.createElement("i");

          icon.className = "material-icons";

          icon.innerHTML = "chevron_right"

          linktoaction.appendChild(icon)
          cardaction.appendChild(linktoaction)

          // Child 5 Fav button

          var linktofav = document.createElement("a");

          linktofav.id = snk['sku'];

          // linktofav.href = snk['link3'];

          linktofav.className = "android-link mdl-button mdl-js-button mdl-typography--text-uppercase";

          linktofav.innerHTML = 'Save ';


          // Adds the saveSneaker() function to the card onclick.

          linktofav.onclick = function() {saveSneakerLite(this.id);}

          var ficon = document.createElement("i");

          var skid = snk['name'];

          ficon.id = skid;

          ficon.className = "material-icons";

          ficon.innerHTML = "favorite_border"

          linktofav.appendChild(ficon)
          cardaction.appendChild(linktofav)



          // Append Childs to Mother

          card.appendChild(cardimg)
          card.appendChild(cardtitle)
          card.appendChild(cardsubtext)
          card.appendChild(cardaction)

          // Append to Sneaker Container

          var sneakercontainer = document.getElementById('sneaker-container-search');

          sneakercontainer.appendChild(card)

          // markSneakerFav(snk['sku']);


          // Ryzen Fourth (R4)
          // RYZEN SUBROUTINE I (R3 Call): Sneaker Checker
          // checkSneakers(skid);

          // console.log(card)

        }

      resolve('resolved');
    }, 2);
  });
}

async function searchdataCall(res) {
  console.log('calling');
  const result = await searchdataProcess(res);
  console.log(result);
  document.getElementById("sneaker-container-search").style.opacity = "0.0";

  // expected output: "resolved"
}
