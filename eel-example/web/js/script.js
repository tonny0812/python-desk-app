var inicialSettings = {
    init: function () {
        inicialSettings.setTitle();
        inicialSettings.loadUsers();
        inicialSettings.loadButton();
        //python可以调用js函数
        eel.expose(my_javascript_function);
        eel.expose(js_random);
    },
    setTitle: function () {
        eel.set_title()().then(function (value) {
            $("h3").text(value);
        });
    },
    loadUsers: function () {
        eel.get_users()().then(function (users) {
            console.log(users);
            var trHTML = '';
            $.each(users, function (i, user) {
                trHTML += '<tr><td>' + user.email + '</td><td>' + user.password + '</td><td>';
            });
            $('#table-body').empty().append(trHTML);
            py_random();
        })
    },
    loadButton: function () {
        $("#submit-button").on('click', function () {
            eel.save_user($("#exampleInputEmail1").val(), $("#exampleInputPassword1").val())
            inicialSettings.loadUsers();
            return false
        });
        $("#delete-button").on('click', function () {
            eel.drop_database()
            inicialSettings.loadUsers();
            return false
        });
    },
};

function my_javascript_function(a, b, c, d) {
  if(a < b){
    console.log(c * d);
  }
  return (c * d)
}

function js_random() {
  return Math.random();
}

async function py_random() {
  // 只要函数前面带有async, 才能在函数内部使用await
  let n = await eel.py_random()();    // Must prefix call with 'await', otherwise it's the same syntax
  console.log('Got this from Python: ' + n);
}

$(document).ready(function () {
    inicialSettings.init();
});