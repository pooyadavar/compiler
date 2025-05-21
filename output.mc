int ulb51(int gvc57, int lnz44) {
    int _f0_state = 0;
_f0_dispatcher:
    switch (_f0_state) {
        case 0: goto _f0_case_0;
        case 1: goto _f0_case_1;
        case 2: goto _f0_end;
    }
    {
    _f0_case_0:
        int trn49 = (gvc57 - (-lnz44));
        _f0_state = 1;
        goto _f0_dispatcher;
    }
    {
    _f0_case_1:
        return trn49;
    }
    {
    _f0_end:
        return 0;
    }
}
int rqh12() {
    int _f1_state = 0;
_f1_dispatcher:
    switch (_f1_state) {
        case 0: goto _f1_case_0;
        case 1: goto _f1_case_1;
        case 2: goto _f1_case_2;
        case 3: goto _f1_case_3;
        case 4: goto _f1_case_4;
        case 5: goto _f1_case_5;
        case 6: goto _f1_case_6;
        case 7: goto _f1_case_7;
        case 8: goto _f1_case_8;
        case 9: goto _f1_case_9;
        case 10: goto _f1_end;
    }
    {
    _f1_case_0:
        int jpo19 = 5;
        _f1_state = 1;
        goto _f1_dispatcher;
    }
    {
    _f1_case_1:
        int unused_0 = 802;
        _f1_state = 2;
        goto _f1_dispatcher;
    }
    {
    _f1_case_2:
        int ddb23 = 10;
        _f1_state = 3;
        goto _f1_dispatcher;
    }
    {
    _f1_case_3:
        int gvc57_0 = jpo19;
        int lnz44_1 = ddb23;
        int _f0_state_2 = 0;
    _f0_dispatcher:
        switch (_f0_state) {
            case 0: goto _f0_case_0;
            case 1: goto _f0_case_1;
            case 2: goto _f0_end;
        }
        {
        _f0_case_0:
            int trn49_3 = (gvc57_0 - (-lnz44_1));
            Variable:
  name: '_f0_state'
 = 1;
            goto _f0_dispatcher;
        }
        {
        _f0_case_1:
            return trn49_3;
        }
        {
        _f0_end:
            return 0;
        }
        _f1_state = 4;
        goto _f1_dispatcher;
    }
    {
    _f1_case_4:
        if (False)
        {
            printf("Unreachable
");
        }
        _f1_state = 5;
        goto _f1_dispatcher;
    }
    {
    _f1_case_5:
        printf("%d\n", tvm86);
        _f1_state = 6;
        goto _f1_dispatcher;
    }
    {
    _f1_case_6:
        while ((!(jpo19 != 5)))
        {
            printf("sample");
        }
        _f1_state = 7;
        goto _f1_dispatcher;
    }
    {
    _f1_case_7:
        int oyg57 = 0;
        _f1_state = 8;
        goto _f1_dispatcher;
    }
    {
    _f1_case_8:
        for (oyg57 = 0; (oyg57 < 5); oyg57 = (oyg57 - (-1)))
        {
            printf("i is %d\n", oyg57);
        }
        _f1_state = 9;
        goto _f1_dispatcher;
    }
    {
    _f1_case_9:
        return 0;
    }
    {
    _f1_end:
        return 0;
    }
}