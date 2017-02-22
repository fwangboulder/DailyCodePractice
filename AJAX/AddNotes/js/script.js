$(function(){

    var model = {
        // check to see if notes exist
        init: function() {
            if (!localStorage.notes) {
                localStorage.notes = JSON.stringify([]);
            }
        },
        // add new note to localStorage
        add: function(obj) {
            var data = JSON.parse(localStorage.notes);
            data.push(obj);
            localStorage.notes = JSON.stringify(data);
        },
        // get a list of notes existed.
        getAllNotes: function() {
            return JSON.parse(localStorage.notes);
        }
    };


    var octopus = {

        // add new note
        addNewNote: function(noteStr) {
            model.add({
                content: noteStr ,
                // store the date to dateSubmitted in this object
                // The date is milliseconds from Jan 1 1970
                dateSubmitted: Date.now()
              });
            view.render();
        },

        // get a list of all notes
        // add .reverse() for reverse view
        getNotes: function() {
            return model.getAllNotes().reverse();
        },

        init: function() {
            model.init();
            view.init();
        }
    };


    var view = {
        init: function() {
            this.noteList = $('#notes');
            var newNoteForm = $('#new-note-form');
            var newNoteContent = $('#new-note-content');
            newNoteForm.submit(function(e){
                octopus.addNewNote(newNoteContent.val());
                newNoteContent.val('');
                e.preventDefault();
            });
            view.render();
        },
        render: function(){
            var htmlStr = '';
            octopus.getNotes().forEach(function(note){
              // add the dateSubmitted
                htmlStr += '<li class="note">'+
                '<span class="note-date">' + new Date(note.dateSubmitted).toString() + '</span>' +
                        note.content +
                    '</li>';
            });
            this.noteList.html( htmlStr );
        }
    };

    octopus.init();
});
