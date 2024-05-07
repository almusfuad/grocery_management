var productModal = $('#productModal');


$(function() {

    // Function to render UI
    function renderProducts(products) {
        var table = '';
        $.each(products, function(index, value) {
            table += '<tr data-id="' + value.product_id + '" data-name="' + value.name + '" data-unit="' + value.uom_id + '" data-price="' + value.price_per_unit + '">' +
                '<td>' + value.name + '</td>' +
                '<td>' + value.uom_id + '</td>' +
                '<td>' + value.price_per_unit + '</td>' +
                '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
        });
        $("table").find('tbody').empty().html(table);
    }

    // JSON data by api call
    $.get(productListApiUrl, function(response) {
        if (response && response.products) {
            console.log(response.products);
            renderProducts(response.products);

            // Search Product
            $('#searchProduct').on("input", function() {
                var searchQuery = $(this).val().toLowerCase();
                console.log(searchQuery);
                // Filter products based on search query
                var filteredProducts = response.products.filter(function(product) {
                    return product.name.toLowerCase().includes(searchQuery);
                });
                // render the filtered products
                renderProducts(filteredProducts);
            });
        }
    });



});


// delete product
$(document).on("click", ".delete-product", function() {
    var tr = $(this).closest('tr');
    var data = {
        product_id: tr.data('id')
    };
    var isDelete = confirm("Are you sure to delete " + tr.data('name') + " item?");
    console.log(data);
    if (isDelete) {
        callApi("POST", productDeleteApiUrl, data);
    }
});


// save product
$('#saveProduct').on("click", function() {
    // update product detail
    var data = $('#productForm').serializeArray();
    var requestPayload = {
        name: null,
        uom_name: null,
        price_per_unit: null
    };
    for (var i = 0; i < data.length; i++) {
        var element = data[i]
        switch (element.name) {
            case 'name':
                requestPayload.name = element.value;
                break;
            case 'uoms':
                requestPayload.uom_name = element.value;
                break;
            case 'price':
                requestPayload.price_per_unit = parseFloat(element.value);
                break;
        }
    }
    callApi("POST", productAddApiUrl, requestPayload);
    console.log(requestPayload);
});

// Search product
$('#searchProduct').on("click", function() {

})

// Modal operation
productModal.on('show.bs.modal', function() {
    $.get(uomListApiUrl, function(response) {
        if (response && response.uom_list) {
            var options = '<option value="">--Select--</option>';
            $.each(response.uom_list, function(index, uom) {
                options += '<option value="' + uom.uom_name + '">' + uom.uom_name + '</option>';
            });
            $("#uoms").empty().html(options);
        }
    });
});

productModal.on('hide.bs.modal', function() {
    $("#id").val('0');
    $("#name, #unit, #price").val('');
    productModal.find('.modal-title').text('Add New Product');
});