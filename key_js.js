    function getToken(t) {
        var e = getStrQuery(t || "")
          , n = store.getState("searchframeLid")
          , a = store.getState("token")
          , i = SparkMD5.hash(e);
        return window.btoa(a + "|" + i + "|" + Date.now() + "|" + n) + "-" + n + "-3"
    }
  


        function getStrQuery(t) {
        var e = t;
        if (Array.isArray(t)) {
            var n = "";
            t.forEach((function(t) {
                var e = t.data;
                if ("TEXT" === t.type)
                    n += e.text.query
            }
            )),
            e = n
        }
        return e || ""
    }



    function getChatPageInitStoreData() {
        var t, e, n = new URL(location.href).search, a = getDataFromDom('script[name="aiTabFrameBaseData"]') || {}, i = urlParamsObjToJson(new URL(location.href).searchParams), r = handleEventParams({
            searchParams: i,
            user: Object.assign(a.user || {}, a.userInfo || {})
        }), o = "pc" !== getPlatform() && (window.location.pathname === PAGE_CONFIG.CHAT.path || isDeepSeekPage() || hitSample(a.sample, "WISE_NEW_CSAITAB", "1")), s = "pc" === getPlatform() && hitSample(a.sample, "PC_AI_SEARCH_ASSISTANT_INDEX_PAGE", "1"), l = "pc" === getPlatform() && hitSample(a.sample, "PC_AI_SEARCH_ASIDE_UPDATE", "1"), c = "pc" === getPlatform() && hitSample(a.sample, "PC_AI_SEARCH_TOP_BAR_SHOW", "1"), u = "pc" === getPlatform() && hitSample(a.sample, "PC_AI_SEARCH_ASSISTANT_INDEX_INPUT", "1"), d = "pc" !== getPlatform() && getSampleVar(a.sample, "SINGLE_LINE_OVERVIEW");
        if (isExtension()) {
            var p = "https://chat.baidu.com";
            Object.assign(a, {
                user: {},
                chatParams: {
                    sse_host: p,
                    sse_ws_host: p,
                    setype: "csaitab"
                },
                urlInfo: {
                    guideWordsUrl: p + "/aichat/api/aitabserver?ctl=guidewords"
                }
            })
        }
        var h = r.oriLid || ""
          , f = r.knowledgeId || ""
          , g = r.shareId || ""
          , m = s && (!r.query || r.isShowHello) && !h && !f && !g;
        return {
            syncSearchParams: n,
            guideWord: "",
            agentList: [],
            firstRankQuery: r.query,
            chatSearchAcitonId: r.chatSearchAcitonId || "",
            oriLid: h,
            apagelid: r.apagelid || "",
            aPageWord: r.aPageWord || "",
            sgeLid: r.sgeLid || "",
            askType: r.askType || "",
            connectPreQuery: r.connectPreQuery || "",
            searchframeLid: o || "pc" === getPlatform() ? a.lid || Date.now() : null == a || null == (t = a.searchframeParams) ? void 0 : t.lid,
            chatSearch: a.chatSearch,
            chatParams: a.chatParams || {},
            preChatParms: {},
            sa: r.sa || "",
            oriSa: r.sa || "",
            pn: 0,
            isShowHello: +r.isShowHello || 0,
            helloInfo: r.helloInfo || {},
            isHistoryLoading: !1,
            enterType: r.enterType || "",
            pcEnterType: r.pcEnterType || "",
            outEnterType: r.outEnterType || "",
            initShowHistory: r.initShowHistory || !1,
            triggerType: r.triggerType || TriggerType.CONVERSATION,
            appUrlParams: {},
            shareId: r.shareId || "",
            shareVersion: r.shareVersion || "",
            lid: "",
            rank: 0,
            topRank: 1,
            shareRankList: [],
            showSelectedBox: !1,
            query: r.query || "",
            qaPairIdDiff: 0,
            agentInfo: r.agentInfo || {},
            agentRank: 0,
            agentSessionCount: 0,
            agentSa: "bkb_agent",
            preQuery: "",
            showScrollToBottomBtn: !1,
            naInjectTime: r.naInjectTime,
            iosSlipPrefetchEnable: r.iosSlipPrefetchEnable,
            startTimeList: r.startTimeList,
            aitab_ct: r.aitab_ct,
            actiontype: r.actiontype,
            imageQuery: {},
            imageQueryLid: {},
            token: a.token || (null == (e = a.searchframeParams) ? void 0 : e.token) || "",
            pcClickInfo: {},
            searchParams: i,
            csextdata: r.csextdata,
            prefetchUrl: [],
            tplname: r.tplname || "",
            srcid: r.srcid || "",
            order: r.order || "",
            upperSearchbox: r.upperSearchbox,
            openInputPanel: r.openInputPanel,
            hideTopAgentList: !1,
            chatStatus: "",
            generateStatus: "",
            curRankInfo: {
                rank: 0
            },
            subEnterType: r.subEnterType || "",
            subSession: {
                entrance: r.subEnterType || "",
                oriLid: "",
                reRank: 0
            },
            blockCmptList: {},
            truncQueryIndexRange: [],
            phoneParams: a.phoneParams || {},
            syncTabData: !1,
            pulldownDisabled: !1,
            firstRankHideQuery: !1,
            showMindMap: !1,
            showSearchResult: !1,
            showWorkspaceType: "",
            workspaceData: {
                wenku: {
                    outlineLid: "",
                    outlineQid: "",
                    pptId: ""
                }
            },
            pptRanks: [],
            withoutStopSseRanks: [],
            messageReadStyle: r.messageReadStyle,
            urlInfo: a.urlInfo,
            singleOverviewType: d || "",
            pluginPromptType: 0,
            chatPageInitialized: !1,
            searchBoxPanel: r.searchBoxPanel || "",
            topBarHeight: r.topBarHeight || "",
            bottomBarHeight: r.bottomBarHeight || "",
            asideActiveId: r.oriLid || r.knowledgeId || "",
            numerologyId: "",
            videoNid: r.videoNid || "",
            videoType: r.videoType || "",
            isNewHomeSample: s,
            isNewAsideSample: l,
            isNewInputSample: u,
            isNewLiuheSample: c,
            showHome: m,
            dqaKey: "",
            chatEntryInfo: {
                type: "default",
                historyEntrySource: ""
            }
        }
    }



    anti_ext: {
      inputT: store.getState("pcInputTime"),
      ck1: a.clickTimeDiff,
      ck9: a.clientX,
      k10: a.clientY
    },


    pcInputTime: Date.now() - store.getState("pcInputFocusTime")
  

        document.addEventListener("mouseup", (function(t) {
        var e = (new Date).getTime() - startTime
          , n = t.clientX
          , a = t.clientY;
        store.dispatch("update", {
            pcClickInfo: {
                clickTimeDiff: e,
                clientX: n,
                clientY: a
            }
        })
    }

     sa: "functab_pic_" + stringCamelCase(null == t ? void 0 : t.buttonId)







    function nanoid$1() {
        var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
          , e = ""
          , n = new Uint8Array(6);
        crypto.getRandomValues(n);
        for (var a = 0; a < 6; a++)
            e += t[n[a] % 63];
        return e
    }


Date.now() + e + nanoid$1(),




 c.prototype.generateAuthorization = function(e, t, n, i, a, s, c) {
                        return a = this.getTimestamp(a),
                        a = r.format("bce-auth-v1/%s/%s/%d", this.ak, a, s || 1800),
                        o("rawSessionKey = %j", a),
                        s = this.hash(a, this.sk),
                        t = this.generateCanonicalUri(t),
                        n = this.queryStringCanonicalization(n || {}),
                        c = (i = this.headersCanonicalization(i || {}, c))[0],
                        i = i[1],
                        o("canonicalUri = %j", t),
                        o("canonicalQueryString = %j", n),
                        o("canonicalHeaders = %j", c),
                        o("signedHeaders = %j", i),
                        e = r.format("%s\n%s\n%s\n%s", e, t, n, c),
                        o("rawSignature = %j", e),
                        o("signingKey = %j", s),
                        t = this.hash(e, s),
                        i.length ? r.format("%s/%s/%s", a, i.join(";"), t) : r.format("%s//%s", a, t)
                    }