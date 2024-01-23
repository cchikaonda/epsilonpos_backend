// batch_admin.js
(function($){
    $(document).ready(function(){
        function toggleBatchNumberInput() {
            var batchNumberField = $('#id_batch_number');
            var batchNumberTextInput = $('#id_batch_number_manual');

            batchNumberTextInput.toggle(batchNumberField.val() === 'manual');
        }

        $('#id_batch_number').change(function(){
            toggleBatchNumberInput();
        });

        toggleBatchNumberInput();
    });
})(django.jQuery);
