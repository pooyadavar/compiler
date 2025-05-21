int dfa68(int beu23, int cdi95) {
    int _f0_state = 0;
_f0_dispatcher:
    switch (_f0_state) {
        case 0: goto _f0_case_0;
        case 1: goto _f0_case_1;
        case 2: goto _f0_end;
    }
    {
    _f0_case_0:
        int wcx29 = (beu23 - (-cdi95));
        _f0_state = 1;
        goto _f0_dispatcher;
    }
    {
    _f0_case_1:
        return wcx29;
    }
    {
    _f0_end:
        return 0;
    }
}
int dvf30() {
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
        int unused_0 = 790;
        _f1_state = 1;
        goto _f1_dispatcher;
    }
    {
    _f1_case_1:
        int lwl97 = 5;
        _f1_state = 2;
        goto _f1_dispatcher;
    }
    {
    _f1_case_2:
        int qtx28 = 10;
        _f1_state = 3;
        goto _f1_dispatcher;
    }
    {
    _f1_case_3:
        int dzh53 = dfa68(lwl97, qtx28);
        _f1_state = 4;
        goto _f1_dispatcher;
    }
    {
    _f1_case_4:
        printf("%d\n", dzh53);
        _f1_state = 5;
        goto _f1_dispatcher;
    }
    {
    _f1_case_5:
        while ((!(lwl97 != 5)))
        {
            printf("sample");
        }
        _f1_state = 6;
        goto _f1_dispatcher;
    }
    {
    _f1_case_6:
        if (False)
        {
            printf("Unreachable
");
        }
        _f1_state = 7;
        goto _f1_dispatcher;
    }
    {
    _f1_case_7:
        int uys50 = 0;
        _f1_state = 8;
        goto _f1_dispatcher;
    }
    {
    _f1_case_8:
        for (uys50 = 0; (uys50 < 5); uys50 = (uys50 - (-1)))
        {
            printf("i is %d\n", uys50);
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