int xup434(int lkv729, int ccn795) {
    int _f2_state = 0;
    int tun970;
_f2_dispatcher:
    switch (_f2_state) {
        case 0: goto _f2_case_0;
        case 1: goto _f2_case_1;
        case 2: goto _f2_case_2;
        case 3: goto _f2_case_3;
        case 4: goto _f2_end;
    }
    {
    _f2_case_0:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f2_state = 1;
        goto _f2_dispatcher;
    }
    {
    _f2_case_1:
        tun970 = (lkv729 - (-ccn795));
        _f2_state = 2;
        goto _f2_dispatcher;
    }
    {
    _f2_case_2:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f2_state = 3;
        goto _f2_dispatcher;
    }
    {
    _f2_case_3:
        return tun970;
    }
    {
    _f2_end:
        return 0;
    }
}
int main() {
    int _f3_state = 0;
    int dpg295;
    int jaa471;
    int mig836;
_f3_dispatcher:
    switch (_f3_state) {
        case 0: goto _f3_case_0;
        case 1: goto _f3_case_1;
        case 2: goto _f3_case_2;
        case 3: goto _f3_case_3;
        case 4: goto _f3_case_4;
        case 5: goto _f3_case_5;
        case 6: goto _f3_case_6;
        case 7: goto _f3_end;
    }
    {
    _f3_case_0:
        mig836 = 3;
        _f3_state = 1;
        goto _f3_dispatcher;
    }
    {
    _f3_case_1:
        jaa471 = 4;
        _f3_state = 2;
        goto _f3_dispatcher;
    }
    {
    _f3_case_2:
        dpg295 = xup434(mig836, jaa471);
        _f3_state = 3;
        goto _f3_dispatcher;
    }
    {
    _f3_case_3:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f3_state = 4;
        goto _f3_dispatcher;
    }
    {
    _f3_case_4:
        printf("%d\n", dpg295);
        _f3_state = 5;
        goto _f3_dispatcher;
    }
    {
    _f3_case_5:
        if (0)
        {
            printf("Unreachable\\n");
        }
        _f3_state = 6;
        goto _f3_dispatcher;
    }
    {
    _f3_case_6:
        return 0;
    }
    {
    _f3_end:
        return 0;
    }
}