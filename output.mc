int ocd79(int xpx85, int cfm45) {
    int _state = 0;
dispatcher:
    switch (_state) {
        case 0: goto case_0;
        case 1: goto case_1;
        case 2: goto case_end;
    }
    {
    case_0:
        int hkx9 = (xpx85 - (-cfm45));
        _state = 1;
        goto dispatcher;
    }
    {
    case_1:
        return hkx9;
    }
    {
    case_end:
        return 0;
    }
}
int wtn20() {
    int _state = 0;
dispatcher:
    switch (_state) {
        case 0: goto case_0;
        case 1: goto case_1;
        case 2: goto case_2;
        case 3: goto case_3;
        case 4: goto case_4;
        case 5: goto case_5;
        case 6: goto case_6;
        case 7: goto case_7;
        case 8: goto case_end;
    }
    {
    case_0:
        int ubf41 = 5;
        _state = 1;
        goto dispatcher;
    }
    {
    case_1:
        int bnl92 = 10;
        _state = 2;
        goto dispatcher;
    }
    {
    case_2:
        int hle26 = ocd79(ubf41, bnl92);
        _state = 3;
        goto dispatcher;
    }
    {
    case_3:
        printf("%d\n", hle26);
        _state = 4;
        goto dispatcher;
    }
    {
    case_4:
        while ((!(ubf41 != 5)))
        {
            printf("sample");
        }
        _state = 5;
        goto dispatcher;
    }
    {
    case_5:
        int xzq70 = 0;
        _state = 6;
        goto dispatcher;
    }
    {
    case_6:
        for (xzq70 = 0; (xzq70 < 5); xzq70 = (xzq70 - (-1)))
        {
            printf("i is %d\n", xzq70);
        }
        _state = 7;
        goto dispatcher;
    }
    {
    case_7:
        return 0;
    }
    {
    case_end:
        return 0;
    }
}