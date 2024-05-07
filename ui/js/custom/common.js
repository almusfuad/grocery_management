var uomListApiUrl = 'http://127.0.0.1:8000/get_uom/';
var productListApiUrl = 'http://127.0.0.1:8000/show_all_product/';
var productAddApiUrl = 'http://127.0.0.1:8000/add_product/';
var productDeleteApiUrl = 'http://127.0.0.1:8000/delete_product/';
var orderCreateApiUrl = 'http://127.0.0.1:8000/create_order/';
var orderListApiUrl = 'http://127.0.0.1:8000/show_order/';


function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        headers: {
            'Content-Type': 'application/json',
        },
        data: JSON.stringify(data),
    }).done(function(msg) {
        window.location.reload();
    });
}