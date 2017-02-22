$(function() {

    var data = {
        lastID: 0,
        items: []
    };


    var octopus = {
        addItem: function() {
            var thisID = ++data.lastID;

            data.items.push({
                id: thisID,
                visible: true
            });
            view.render();
        },

        removeItem: function(item) {
            var clickedItem = data.items[ item.id - 1 ];
            clickedItem.visible = false;
            view.render();
        },

        getVisibleItems: function() {
            var visibleItems = data.items.filter(function(item) {
                return item.visible;
            });
            return visibleItems;
        },

        init: function() {
            view.init();
        }
    };


    var view = {
        init: function() {
            var addItemBtn = $('.add-item');
            addItemBtn.click(function() {
                octopus.addItem();
            });

            // grab elements and html for using in the render function
            this.$itemList = $('.item-list');
            this.itemTemplate = $('script[data-template="item"]').html();

            // Delegated event to listen for removal clicks
            this.$itemList.on('click', '.remove-item', function(e) {
                var item = $(this).parents('.item').data();
                octopus.removeItem(item);
                return false;
            });

            this.render();
        },

        render: function() {
            // Cache vars for use in forEach() callback (performance)
            var $itemList = this.$itemList,
                itemTemplate = this.itemTemplate;

            // Clear and render
            $itemList.html('');
            octopus.getVisibleItems().forEach(function(item) {
                // Replace template markers with data
                var thisTemplate = itemTemplate.replace(/{{id}}/g, item.id);
                $itemList.append(thisTemplate);
            });
        }
    };

    octopus.init();
}());
