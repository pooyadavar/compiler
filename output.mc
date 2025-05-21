int qai23(int bwu70, int mlf71) {
    int _f0_state = 0;
    int lxw33;
_f0_dispatcher:
    switch (_f0_state) {
        case 0: goto _f0_case_0;
        case 1: goto _f0_case_1;
        case 2: goto _f0_end;
    }
    {
    _f0_case_0:
        lxw33 = (bwu70 - (-mlf71));
        _f0_state = 1;
        goto _f0_dispatcher;
    }
    {
    _f0_case_1:
        return lxw33;
    }
    {
    _f0_end:
        return 0;
    }
}
int jsx33() {
    int _f1_state = 0;
_f1_dispatcher:
    switch (_f1_state) {
        case 0: goto _f1_case_0;
        case 1: goto _f1_case_1;
        case 2: goto _f1_case_2;
        case 3: goto _f1_case_3;
        case 4: goto _f1_case_4;
        case 5: goto _f1_case_5;
        case 6: goto _f1_end;
    }
    {
    _f1_case_0:
        int ueu46 = 3;
        _f1_state = 1;
        goto _f1_dispatcher;
    }
    {
    _f1_case_1:
        int ahf45 = 4;
        _f1_state = 2;
        goto _f1_dispatcher;
    }
    {
    _f1_case_2:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f1_state = 3;
        goto _f1_dispatcher;
    }
    {
    _f1_case_3:
        int rne28 = qai23(ueu46, ahf45);
        _f1_state = 4;
        goto _f1_dispatcher;
    }
    {
    _f1_case_4:
        printf("%d\n", rne28);
        _f1_state = 5;
        goto _f1_dispatcher;
    }
    {
    _f1_case_5:
        return 0;
    }
    {
    _f1_end:
        return 0;
    }
}