// Memory Game
// © 2014 Nate Wiley
// License -- MIT
// best in full screen, works on phones/tablets (min height for game is 500px..) enjoy ;)
// Follow me on Codepen

(function () {
  var Memory = {
    init: function (cards) {
      this.$game = $(".game");
      this.$modal = $(".modal");
      this.$overlay = $(".modal-overlay");
      this.$restartButton = $("button.restart");
      this.cardsArray = $.merge(cards, cards);
      this.shuffleCards(this.cardsArray);
      this.setup();
    },

    shuffleCards: function (cardsArray) {
      this.$cards = $(this.shuffle(this.cardsArray));
    },

    setup: function () {
      this.html = this.buildHTML();
      this.$game.html(this.html);
      this.$memoryCards = $(".card");
      this.paused = false;
      this.guess = null;
      this.binding();
    },

    binding: function () {
      this.$memoryCards.on("click", this.cardClicked);
      this.$restartButton.on("click", $.proxy(this.reset, this));
    },
    // kinda messy but hey
    cardClicked: function () {
      var _ = Memory;
      var $card = $(this);
      if (
        !_.paused &&
        !$card.find(".inside").hasClass("matched") &&
        !$card.find(".inside").hasClass("picked")
      ) {
        $card.find(".inside").addClass("picked");
        if (!_.guess) {
          _.guess = $(this).attr("data-id");
        } else if (
          _.guess == $(this).attr("data-id") &&
          !$(this).hasClass("picked")
        ) {
          $(".picked").addClass("matched");
          _.guess = null;
        } else {
          _.guess = null;
          _.paused = true;
          setTimeout(function () {
            $(".picked").removeClass("picked");
            Memory.paused = false;
          }, 600);
        }
        if ($(".matched").length == $(".card").length) {
          _.win();
        }
      }
    },

    win: function () {
      this.paused = true;
      setTimeout(function () {
        Memory.showModal();
        Memory.$game.fadeOut();
      }, 1000);
    },

    showModal: function () {
      this.$overlay.show();
      this.$modal.fadeIn("slow");
    },

    hideModal: function () {
      this.$overlay.hide();
      this.$modal.hide();
    },

    reset: function () {
      this.hideModal();
      this.shuffleCards(this.cardsArray);
      this.setup();
      this.$game.show("slow");
    },

    // Fisher--Yates Algorithm -- https://bost.ocks.org/mike/shuffle/
    shuffle: function (array) {
      var counter = array.length,
        temp,
        index;
      // While there are elements in the array
      while (counter > 0) {
        // Pick a random index
        index = Math.floor(Math.random() * counter);
        // Decrease counter by 1
        counter--;
        // And swap the last element with it
        temp = array[counter];
        array[counter] = array[index];
        array[index] = temp;
      }
      return array;
    },

    buildHTML: function () {
      var frag = "";
      this.$cards.each(function (k, v) {
        frag +=
          '<div class="card" data-id="' +
          v.id +
          '"><div class="inside">\
                  <div class="front"><img src="' +
          v.img +
          '"\
                  alt="' +
          v.name +
          '" /></div>\
                  <div class="back"><img src="static/Home/images/dominators.jpg"\
                  alt="Codepen" /></div></div>\
                  </div>';
      });
      return frag;
    },
  };

  var cards = [
    {
      name: "football",
      img: "static/Home/images/360_F_32709219_eUEJoIqlKuOqpOMkGSR6QI9sNsA2djS7.jpg",
      id: 1,
    },
    {
      name: "bulb",
      img: "static/Home/images/360_F_338701333_RKkDsySJecJMRx4aNFh7WJvxBUIi6CtN.webp",
      id: 2,
    },
    {
      name: "camera",
      img: "static/Home/images/retro-camera_144627-12239.webp",
      id: 3,
    },
    {
      name: "nemo",
      img: "static/Home/images/1805523.webp",
      id: 4,
    },
    {
      name: "cricket",
      img: "static/Home/images/239835.webp",
      id: 5,
    },
    {
      name: "dice",
      img: "static/Home/images/dice.webp",
      id: 6,
    },
    {
      name: "apple",
      img: "static/Home/images/photo-1579613832125-5d34a13ffe2a.webp",
      id: 7,
    },
    {
      name: "python",
      img: "https://s3-us-west-2.amazonaws.com/s.cdpn.io/74196/python-logo.png",
      id: 8,
    },
    {
      name: "flower",
      img: "static/Home/images/random-1574391.webp",
      id: 9,
    },
    {
      name: "swan",
      img: "static/Home/images/swan-2107052_640.webp",
      id: 10,
    },
    {
      name: "tree",
      img: "static/Home/images/grassy-landscape-with-tree-raincloud_1048-2904.webp",
      id: 11,
    },
    {
      name: "butterfly",
      img: "static/Home/images/closeup-shot-beautiful-butterfly-with-interesting-textures-orange-petaled-flower_181624-7640.webp",
      id: 12,
    },
  ];

  Memory.init(cards);
})();
