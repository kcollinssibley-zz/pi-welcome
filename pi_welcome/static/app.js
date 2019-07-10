$.support.cors = true;  //global

ko.bindingHandlers.dateTime =
{
    update: function (element, valueAccessor, allBindingsAccessor, viewModel)
    {
        var val = valueAccessor();

        var formatted = "";
        var date = moment(ko.utils.unwrapObservable(val));
        var format = allBindingsAccessor().format || 'MMM D, YYYY h:mm A'; //default format

        if (date && date.isValid())
        {
            formatted = date.format(format);
        }

        element.innerHTML = formatted;
    }
};

ko.bindingHandlers.date =
{
    update: function (element, valueAccessor, allBindingsAccessor, viewModel)
    {
        var val = valueAccessor();

        var formatted = "";
        var date = moment.utc(ko.utils.unwrapObservable(val));
        var format = allBindingsAccessor().format || 'M/D/YYYY'; //default format

        if (date && date.isValid())
        {
            formatted = date.format(format);
        }

        element.innerHTML = formatted;
    }
};

ko.bindingHandlers.time =
{
    update: function (element, valueAccessor, allBindingsAccessor, viewModel)
    {
        var val = valueAccessor();

        var formatted = "";
        var date = moment(ko.utils.unwrapObservable(val));
        var format = allBindingsAccessor().format || 'h:mm A'; //default format

        if (date && date.isValid())
        {
            formatted = date.format(format);
        }

        element.innerHTML = formatted;
    }
};

ko.bindingHandlers.fromNow =
{
    update: function (element, valueAccessor, allBindingsAccessor, viewModel)
    {
        var val = valueAccessor();

        var fromNow = "";
        var date = moment(ko.utils.unwrapObservable(val));
        //var format = allBindingsAccessor().format || 'MMM D, YYYY h:mm A'; //default format

        if (date && date.isValid())
        {
            //formatted = date.format(format);
            fromNow = date.fromNow();
        }

        element.innerHTML = fromNow;
    }
};

ko.bindingHandlers.friendlyBool =
{
    update: function (element, valueAccessor, allBindingsAccessor)
    {
        var value = ko.utils.unwrapObservable(valueAccessor()) || false;

        element.innerHTML = (value == true) ? "Yes" : "No";
    }
}


ko.bindingHandlers.bootstrapModal =
{
    init: function (element, valueAccessor)
    {
        $(element).modal({
            show: false
        });

        var value = valueAccessor();
        if (ko.isObservable(value))
        {
            $(element).on('hide.bs.modal', function ()
            {
                value(false);
            });


            //kendo dropdownlists are windowed, and conflict with bootstrap 3 focusing on modals, this seems to fix...
            //http://stackoverflow.com/questions/14795035/twitter-bootstrap-modal-blocks-text-input-field/14795256
            $(element).on('shown.bs.modal', function ()
            {
                $(document).off('focusin.modal');
            });
        }
        ko.utils.domNodeDisposal.addDisposeCallback(element, function ()
        {
            $(element).modal("destroy");
        });

    },
    update: function (element, valueAccessor)
    {
        var value = valueAccessor();
        if (ko.utils.unwrapObservable(value))
        {
            $(element).modal('show');
        } else
        {
            $(element).modal('hide');
        }
    }
}


getValidationErrors = function (error)
{
    if (!error.responseJSON)
    {
        return null;
    }

    if (!error.responseJSON.ResponseStatus)
    {
        return null;
    }

    if (error.responseJSON.ResponseStatus.Errors.length == 0)
    {
        return null;
    }

    return error.responseJSON.ResponseStatus.Errors
}

ko.bindingHandlers.dropzone =
{
    init: function (element, valueAccessor)
    {
        var value = ko.unwrap(valueAccessor());

        var options = {
            maxFileSize: 15,
            createImageThumbnails: false,
        };

        $.extend(options, value);

        $(element).addClass('dropzone');
        new Dropzone(element, options); // jshint ignore:line
    }
};

ko.bindingHandlers.percent =
{
    update: function (element, valueAccessor, allBindingsAccessor, viewModel)
    {
        var val = parseFloat(ko.utils.unwrapObservable(valueAccessor()));
        var percent = "0";
        if (!isNaN(val))
        {
            percent = (val * 100).toFixed(2);
        }

        element.innerHTML = percent + "%";
    }
}

ko.bindingHandlers.sort =
{
    'init': function (element, valueAccessor, allBindingsAccessor, viewModel, bindingContext)
    {
        var originalFunction = valueAccessor();
        var column = allBindingsAccessor().column; //sort column
        element.style.cursor = 'pointer';

        var newValueAccesssor = function ()
        {
            return function (event)
            {
                var thElements = element.parentNode.children;
                if (thElements.length)
                {
                    for (var i = 0; i < thElements.length; i++)
                    {
                        thElements[i].className = "";
                    }
                }
                if (column != viewModel.sortColumn)
                {
                    viewModel.sortColumn = column;
                    viewModel.sortDirection = "DESC";
                    element.className = "sortDesc"; // glyphicon glyphicon-triangle-top
                }
                else
                {
                    if (viewModel.sortDirection == "ASC")
                    {
                        viewModel.sortDirection = "DESC";
                        element.className = "sortDesc"; // glyphicon glyphicon-triangle-bottom
                    }
                    else
                    {
                        viewModel.sortDirection = "ASC";
                        element.className = "sortAsc"; // glyphicon glyphicon-triangle-top
                    }
                }

                //pass through the arguments
                originalFunction.apply(viewModel, arguments);
            }
        }
        ko.bindingHandlers.click.init(element, newValueAccesssor,
            allBindingsAccessor, viewModel, bindingContext);
    }
}


ko.bindingHandlers.truncatedText =
{
    update: function (element, valueAccessor, allBindingsAccessor)
    {
        var originalText = ko.utils.unwrapObservable(valueAccessor());
            // 10 is a default maximum length

        if (originalText != null)
        {
            var length = ko.utils.unwrapObservable(allBindingsAccessor().maxTextLength) || 20;
            var truncatedText = originalText.length > length ? originalText.substring(0, length) + "..." : originalText;


            // updating text binding handler to show truncatedText
            ko.bindingHandlers.text.update(element, function ()
            {
                return truncatedText;
            });

        }
    }
};

ko.bindingHandlers.currency =
{
    symbol: ko.observable('$'),
    update: function (element, valueAccessor, allBindingsAccessor)
    {
        return ko.bindingHandlers.text.update(element, function ()
        {
            var value = +(ko.utils.unwrapObservable(valueAccessor()) || 0);
            var symbol = ko.utils.unwrapObservable(allBindingsAccessor().symbol != undefined ? allBindingsAccessor().symbol : ko.bindingHandlers.currency.symbol);

            var finalValue = symbol + Math.abs(value).toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, "$1,");
            if (value < 0)
            {
                finalValue = "(" + finalValue + ")";
            }

            return finalValue;
        });
    }
};

window.onerror = function (message, file, line, col, error)
{
    showError(message);
};

showError = function(error)
{
    var errorMessage;
    if (typeof error === "string")
    {
        errorMessage = error;
    }
    else
    {
        errorMessage = error.status + " - " + error.statusText;
    }

    alert(errorMessage);
    //ko.postbox.publish("error-modal-message", errorMessage); //the z index of this modal wont force error modal in front of another open modal, like the user edit modal...research this more.
};
