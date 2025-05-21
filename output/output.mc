int ipj1(int mvd353, int lli209) {
    int _f0_state = 0;
    int szq25;
_f0_dispatcher:
    switch (_f0_state) {
        case 0: goto _f0_case_0;
        case 1: goto _f0_case_1;
        case 2: goto _f0_end;
    }
    {
    _f0_case_0:
        szq25 = (mvd353 - (-lli209));
        _f0_state = 1;
        goto _f0_dispatcher;
    }
    {
    _f0_case_1:
        return szq25;
    }
    {
    _f0_end:
        return 0;
    }
}
int main() {
    int _f1_state = 0;
    int i;
    int mpw457;
    int qix614;
    int ueq586;
    int unused_0;
    int uyn462;
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
        case 10: goto _f1_case_10;
        case 11: goto _f1_end;
    }
    {
    _f1_case_0:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f1_state = 1;
        goto _f1_dispatcher;
    }
    {
    _f1_case_1:
        qix614 = 5;
        _f1_state = 2;
        goto _f1_dispatcher;
    }
    {
    _f1_case_2:
        uyn462 = 10;
        _f1_state = 3;
        goto _f1_dispatcher;
    }
    {
    _f1_case_3:
        unused_0 = 149;
        _f1_state = 4;
        goto _f1_dispatcher;
    }
    {
    _f1_case_4:
        mpw457 = ipj1(qix614, uyn462);
        _f1_state = 5;
        goto _f1_dispatcher;
    }
    {
    _f1_case_5:
        printf("%d\n", mpw457);
        _f1_state = 6;
        goto _f1_dispatcher;
    }
    {
    _f1_case_6:
        while ((!(qix614 != 5)))
        {
            printf("sample");
            x = 0;
        }
        _f1_state = 7;
        goto _f1_dispatcher;
    }
    {
    _f1_case_7:
        ueq586 = 0;
        _f1_state = 8;
        goto _f1_dispatcher;
    }
    {
    _f1_case_8:
        for (; i = (ueq586 - (-1)); )
        {
            printf("i is %d\n", ueq586);
        }
        _f1_state = 9;
        goto _f1_dispatcher;
    }
    {
    _f1_case_9:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f1_state = 10;
        goto _f1_dispatcher;
    }
    {
    _f1_case_10:
        return 0;
    }
    {
    _f1_end:
        return 0;
    }
}