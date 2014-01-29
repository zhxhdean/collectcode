(function(docu) {

    var objxttop = null; //topdiv对象

    var xttop = function(topjason) {

        var doc = document,

        docbody = doc.body,

        goto_top_type = -1, //记录浏览器类型

        goto_top_itv = 0,

        isNotIE = -[ -1 , ]; //全世界最短的判断IE浏览器,非IE浏览器为1,IE为NAN

        config = topjason || {};

        var div = doc.createElement("div");
        div.id = config["id"] || "xttop"; //topdiv设置ID,默认为xttop,为避免冲突,请自设
        div.style.cssText = "position:fixed;bottom:" + (config["bottom"] || "100px") + ";right:" + (config["right"] || "0") + ";display:none;width:" + (config["width"] || "50px") + ";height:" + (config["height"] || "100px") + ";";
        
        var topdiv = doc.createElement("div");

    

        //topdiv样式

        div.innerHTML = '<div id="comments-link"><a href="#comment"  title="点评" class="comments"><span class="leave-reply">点评</span></a></div>'
        	

        if (config["img"]) {
        	topdiv.style.cssText ="width:43px;height:45px;"
            topdiv.style.background = "url(" + (config["img"] == "defaults" ? "http://www.exiatian.com/wp-content/themes/thunder/images/top.png": config["img"]) + ") no-repeat -5px -2px"; //加上背景图片

        } else {

            topdiv.innerHTML = "<span style='color:#7B8693;font-size:12px;border:1px solid #7B8693;'>↑顶部</span>"; //默认以文字展示

        }

        function goto_top_timer() {

            var y = docbody.scrollTop|| doc.documentElement.scrollTop;

            var moveby = config["speed"] || 35;



            y -= Math.ceil(y * moveby / 100); //匀减速

            if (y < 0) {

                y = 0;

            }



            if ( docbody.scrollTop ) {

                    docbody.scrollTop = y;

            } else {

                doc.documentElement.scrollTop = y;

            }



            if (y == 0) {

                clearInterval(goto_top_itv);

                goto_top_itv = 0;

            }

        }

        function goto_top() {

            if (goto_top_itv == 0) {

                goto_top_itv = setInterval(goto_top_timer, 50);

            }

        }

        bind(topdiv, "click", goto_top);
        div.appendChild(topdiv)
        docbody.appendChild(div);

    }



    var bind = function(object, type, fn) {

        if (object.attachEvent) { //IE浏览器

            object.attachEvent("on" + type, (function() {

                return function() {

                    window.event.cancelBubble = true; //停止时间冒泡

                    object.attachEvent = fn.apply(object);

                }

            })(object));

        } else if (object.addEventListener) { //其他浏览器

            object.addEventListener(type,

            function(event) {

                event.stopPropagation(); //停止时间冒泡

                fn.apply(this)

            },

            false);

        }

    }

    var scrollevent = function() {

        objxttop = objxttop || document.getElementById("xttop");

        if (document.documentElement.scrollTop > 120 || document.body.scrollTop > 120) //当IE或其他浏览器滚动条值大于120时,top显示出来

        {

            objxttop.style.display = "block";

        } else //小于120时,top隐藏

        {

            objxttop.style.display = "none";

        }

    }

    window.xttop = xttop;

    window.onscroll = scrollevent; //绑定滚动条事件

})();