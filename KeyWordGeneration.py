
    def genarate(list1, list2, data):

        founds = []
        twoWordsCombine = [list1,list2]
        threeWordsCombine1 = [list1,list2,list1]
        threeWordsCombine2 = [list1,list2,list2]
        fourWordsCombine1 = [list1,list2,list1,list2]
        fourWordsCombine2 = [list1,list2,list2,list1]

        list1 = list(itertools.product(*twoWordsCombine))
        list2 = list(itertools.product(*threeWordsCombine1))
        list3 = list(itertools.product(*threeWordsCombine2))
        list4 = list(itertools.product(*fourWordsCombine1))
        list5 = list(itertools.product(*fourWordsCombine2))