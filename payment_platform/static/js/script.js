function payWithPaystack(){
    let currency = 'NGN';
    let plan = '';
    let ref = '{{ payment.ref }}'
    let obj = {
        key: '{{ paystack_public_key }}',
        email: '{{ payment.email }}',
        amount: '{{ payment.amount }}',
        ref : ref
        callback: function(response){
            window.location.href = '{% url 'verify-payment' payment.ref %}'
        }
    }
    if(Boolean(currency)){
        obj.currency = currency.toUpperCase()
    }
    if(Boolean(plan)){
        obj.plan = plan;
    }
    var handler = PaystackPop.setup(obj);
    handler.openIframe
}