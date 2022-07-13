$(function () {
    $('.selectall').click(function () {
        $('.selectbox').prop('checked', $(this).prop('checked'));
    });

    $('.selectbox').change(function () {
        var total = $('.selectbox').length;
        var number = $('.selectbox:checked').length;
        if (total == number) {
            $('.selectall').prop('checked', true);
        } else {
            $('.selectall').prop('checked', false);
        }
    });
});