int jlp673(int ktc54, int ifc842) {
    int _f0_state = 0;
    int lan900;
_f0_dispatcher:
    switch (_f0_state) {
        case 0: goto _f0_case_0;
        case 1: goto _f0_case_1;
        case 2: goto _f0_end;
    }
    {
    _f0_case_0:
        lan900 = (ktc54 - (-ifc842));
        _f0_state = 1;
        goto _f0_dispatcher;
    }
    {
    _f0_case_1:
        return lan900;
    }
    {
    _f0_end:
        return 0;
    }
}
int main() {
    int _f1_state = 0;
    int hfu508;
    int i;
    int kqh858;
    int ssn932;
    int tud211;
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
        case 8: goto _f1_case_8;
        case 9: goto _f1_case_9;
        case 10: goto _f1_case_10;
        case 11: goto _f1_end;
    }
    {
    _f1_case_0:
        kqh858 = 5;
        _f1_state = 1;
        goto _f1_dispatcher;
    }
    {
    _f1_case_1:
        ssn932 = 10;
        _f1_state = 2;
        goto _f1_dispatcher;
    }
    {
    _f1_case_2:
        hfu508 = jlp673(kqh858, ssn932);
        _f1_state = 3;
        goto _f1_dispatcher;
    }
    {
    _f1_case_3:
        printf("%d\n", hfu508);
        _f1_state = 4;
        goto _f1_dispatcher;
    }
    {
    _f1_case_4:
        unused_0 = 423;
        _f1_state = 5;
        goto _f1_dispatcher;
    }
    {
    _f1_case_5:
        while ((!(kqh858 != 5)))
        {
            printf("sample");
            if (0)
            {
                printf("Unreachable\\n");
            }
            x = 0;
        }
        _f1_state = 6;
        goto _f1_dispatcher;
    }
    {
    _f1_case_6:
        tud211 = 0;
        _f1_state = 7;
        goto _f1_dispatcher;
    }
    {
    _f1_case_7:
        unused_1 = 672;
        _f1_state = 8;
        goto _f1_dispatcher;
    }
    {
    _f1_case_8:
        for (; i = (tud211 - (-1)); )
        {
            if (0)
            {
                printf("Unreachable\\n");
            }
            printf("i is %d\n", tud211);
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