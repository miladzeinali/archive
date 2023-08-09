$( document ).ready(function() {
    function isNumber(n) {
        return !isNaN(parseFloat(n)) && isFinite(n);
      }
      
      function setFontSize(el) {
          var fontSize = el.val();
          
          if ( isNumber(fontSize) && fontSize >= 0.5 ) {
            $('body').css({ fontSize: fontSize + 'em' });
          } else if ( fontSize ) {
            el.val('1');
            $('body').css({ fontSize: '1em' });  
          }
      }
      
      $(function() {
        
        $('#fontSize')
          .bind('change', function(){ setFontSize($(this)); })
          .bind('keyup', function(e){
            if (e.keyCode == 27) {
              $(this).val('1');
              $('body').css({ fontSize: '1em' });  
            } else {
              setFontSize($(this));
            }
          });
        
        $(window)
          .bind('keyup', function(e){
            if (e.keyCode == 27) {
              $('#fontSize').val('1');
              $('body').css({ fontSize: '1em' });  
            }
          });
        
      });
    
      $(function() {
        let treeview = {
          resetBtnToggle: function() {
            $(".js-treeview")
              .find(".level-add")
              .find("span")
              .removeClass()
              .addClass("fa fa-plus");
            $(".js-treeview")
              .find(".level-add")
              .siblings()
              .removeClass("in");
          },
          addSameLevel: function(target) {
            let ulElm = target.closest("ul");
            let sameLevelCodeASCII = target
              .closest("[data-level]")
              .attr("data-level")
              .charCodeAt(0);
            ulElm.append($("#levelMarkup").html());
            ulElm
              .children("li:last-child")
              .find("[data-level]")
              .attr("data-level", String.fromCharCode(sameLevelCodeASCII));
          },
          addSubLevel: function(target) {
            let liElm = target.closest("li");
            let nextLevelCodeASCII = liElm.find("[data-level]").attr("data-level").charCodeAt(0) + 1;
            liElm.children("ul").append($("#levelMarkup").html());
            liElm.children("ul").find("[data-level]")
              .attr("data-level", String.fromCharCode(nextLevelCodeASCII));
          },
          removeLevel: function(target) {
            target.closest("li").remove();
            
          }
        };
      
        // Treeview Functions
        $(".js-treeview").on("click", ".level-add", function() {
          $(this).find("span").toggleClass("fa-plus").toggleClass("fa-times text-danger");
          $(this).siblings().toggleClass("in");
        });
      
        // Add same level
        $(".js-treeview").on("click", ".level-same", function() {
          treeview.addSameLevel($(this));
          treeview.resetBtnToggle();
        });
      
        // Add sub level
        $(".js-treeview").on("click", ".level-sub", function() {
          treeview.addSubLevel($(this));
          treeview.resetBtnToggle();
        });
          // Remove Level
        $(".js-treeview").on("click", ".level-remove", function() {
          treeview.removeLevel($(this));
        }); 
      
        // Selected Level
        $(".js-treeview").on("click", ".level-title", function() {
          let isSelected = $(this).closest("[data-level]").hasClass("selected");
          !isSelected && $(this).closest(".js-treeview").find("[data-level]").removeClass("selected");
          $(this).closest("[data-level]").toggleClass("selected");
        }); 
      });
});
