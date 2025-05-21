int ieb724(int jsc240, int uhs315) {
    int _f0_state = 0;
    int isp39;
_f0_dispatcher:
    switch (_f0_state) {
        case 0: goto _f0_case_0;
        case 1: goto _f0_case_1;
        case 2: goto _f0_case_2;
        case 3: goto _f0_end;
    }
    {
    _f0_case_0:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f0_state = 1;
        goto _f0_dispatcher;
    }
    {
    _f0_case_1:
        isp39 = (jsc240 - (-uhs315));
        _f0_state = 2;
        goto _f0_dispatcher;
    }
    {
    _f0_case_2:
        return isp39;
    }
    {
    _f0_end:
        return 0;
    }
}
int main() {
    int _f1_state = 0;
    int mdh194;
    int qmm162;
    int qrs745;
    int unused_0;
    int unused_1;
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
        case 8: goto _f1_end;
    }
    {
    _f1_case_0:
        mdh194 = 3;
        _f1_state = 1;
        goto _f1_dispatcher;
    }
    {
    _f1_case_1:
        unused_0 = 224;
        _f1_state = 2;
        goto _f1_dispatcher;
    }
    {
    _f1_case_2:
        qrs745 = 4;
        _f1_state = 3;
        goto _f1_dispatcher;
    }
    {
    _f1_case_3:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f1_state = 4;
        goto _f1_dispatcher;
    }
    {
    _f1_case_4:
        qmm162 = ieb724(mdh194, qrs745);
        _f1_state = 5;
        goto _f1_dispatcher;
    }
    {
    _f1_case_5:
        printf("%d\n", qmm162);
        _f1_state = 6;
        goto _f1_dispatcher;
    }
    {
    _f1_case_6:
        unused_1 = 237;
        _f1_state = 7;
        goto _f1_dispatcher;
    }
    {
    _f1_case_7:
        return 0;
    }
    {
    _f1_end:
        return 0;
    }
}