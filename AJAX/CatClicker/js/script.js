// Interaction:
// When a cat name is clicked in the list, the cat display area should update
//to show the data for the selected cat.
// The number of clicks in the cat area should be unique to each cat, and
//should increment when the cat's picture is clicked.

// Add Model Octopus and View
// Model:
// Octopus:
// View: two views, one is for the cat list and the other is for the cat detail views
//CatView and CatListView, each view has its own render methods.
var model = {
		//data currentCat and Cats list
    currentCat: null,
    cats: [
        {
            clickCount : 0,
            name : 'Alpha',
            imgSrc : 'img/1.jpg',
        },
        {
            clickCount : 0,
            name : 'Little Fish',
            imgSrc : 'img/2.jpg',
        },
        {
            clickCount : 0,
            name : 'Easy',
            imgSrc : 'img/3.jpg',
        }
    ]
};

var octopus = {

    init: function() {
        // set our current cat to the first one in the list
        model.currentCat = model.cats[0];

        // tell our views to initialize
				//
        catListView.init();

        catView.init();
    },

    getCurrentCat: function() {
        return model.currentCat;
    },
		//return all cats list
    getCats: function() {
        return model.cats;
    },

    // set the currently-selected cat to the object passed in
    setCurrentCat: function(cat) {
        model.currentCat = cat;
    },

    // increments the counter for the currently-selected cat
    incrementCounter: function() {
        model.currentCat.clickCount++;
				//update the catView
        catView.render();
    }
};

var catView = {

    init: function() {
        // store pointers to our DOM elements for easy access later
        this.catElem = document.getElementById('cat');
        this.catNameElem = document.getElementById('cat-name');
        this.catImageElem = document.getElementById('cat-img');
        this.countElem = document.getElementById('cat-count');

        // on click, increment the current cat's counter
        this.catImageElem.addEventListener('click', function(){
            octopus.incrementCounter();
        });

        // render this view (update the DOM elements with the right values)
        this.render();
    },

    render: function() {
        // update the DOM elements with values from the current cat
        var currentCat = octopus.getCurrentCat();
        this.countElem.textContent = currentCat.clickCount+' clicks';
        this.catNameElem.textContent = 'Current Cat: '+ currentCat.name;
        this.catImageElem.src = currentCat.imgSrc;
    }
};

var catListView = {

    init: function() {
        // store the DOM element for easy access later
        this.catListElem = document.getElementById('cat-list');

        // render this view (update the DOM elements with the right values)
        this.render();
    },

    render: function() {
        var cat, elem, i;
        // get the cats we'll be rendering from the octopus
        var cats = octopus.getCats();

        // empty the cat list
        this.catListElem.innerHTML = '';

        // loop over the cats
        for (i = 0; i < cats.length; i++) {
            // this is the cat we're currently looping over
            cat = cats[i];

            // make a new cat list item and set its text
            elem = document.createElement('h1');
            elem.textContent =  cat.name;

            // on click, setCurrentCat and render the catView
            // (this uses our closure-in-a-loop trick to connect the value
            //  of the cat variable to the click event function)
            elem.addEventListener('click', (function(catCopy) {
                return function() {
                    octopus.setCurrentCat(catCopy);
                    catView.render();
                };
            })(cat));

            // finally, add the element to the list
            this.catListElem.appendChild(elem);
        }
    }
};

// make it go!
octopus.init();
