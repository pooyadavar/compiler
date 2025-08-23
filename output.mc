int ypl269(int ojc455, int frl723) {
    int _f0_state = 0;
    int unused_0;
    int xvy170;
_f0_dispatcher:
    switch (_f0_state) {
        case 0: goto _f0_case_0;
        case 1: goto _f0_case_1;
        case 2: goto _f0_case_2;
        case 3: goto _f0_case_3;
        case 4: goto _f0_end;
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
        xvy170 = (ojc455 - (-frl723));
        _f0_state = 2;
        goto _f0_dispatcher;
    }
    {
    _f0_case_2:
        unused_0 = 671;
        _f0_state = 3;
        goto _f0_dispatcher;
    }
    {
    _f0_case_3:
        return xvy170;
    }
    {
    _f0_end:
        return 0;
    }
}
int main() {
    int _f1_state = 0;
    int bjd83;
    int i;
    int mty105;
    int naq344;
    int rhh288;
    int unused_1;
    int unused_2;
    int unused_3;
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
        unused_1 = 536;
        _f1_state = 1;
        goto _f1_dispatcher;
    }
    {
    _f1_case_1:
        rhh288 = 5;
        _f1_state = 2;
        goto _f1_dispatcher;
    }
    {
    _f1_case_2:
        naq344 = 10;
        _f1_state = 3;
        goto _f1_dispatcher;
    }
    {
    _f1_case_3:
        bjd83 = ypl269(rhh288, naq344);
        _f1_state = 4;
        goto _f1_dispatcher;
    }
    {
    _f1_case_4:
        printf("%d\n", bjd83);
        _f1_state = 5;
        goto _f1_dispatcher;
    }
    {
    _f1_case_5:
        while ((!(rhh288 != 5)))
        {
            if (0)
            {
                printf("Unreachable\\n");
            }
            printf("sample");
        }
        _f1_state = 6;
        goto _f1_dispatcher;
    }
    {
    _f1_case_6:
        mty105 = 0;
        _f1_state = 7;
        goto _f1_dispatcher;
    }
    {
    _f1_case_7:
        unused_2 = 966;
        _f1_state = 8;
        goto _f1_dispatcher;
    }
    {
    _f1_case_8:
        for (; i = (mty105 - (-1)); )
        {
            printf("i is %d\n", mty105);
        }
        _f1_state = 9;
        goto _f1_dispatcher;
    }
    {
    _f1_case_9:
        unused_3 = 914;
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