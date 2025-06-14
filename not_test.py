import cocotb
from cocotb.triggers import Timer, RisingEdge 

@cocotb.test()
async def not_test(dut):
    a={0,1}
    y={1,0}

    for i in range(2)
    dut.a.value=a[i]
    await Timer(1,'ns')
    assert dut.y.value == y[i] , f"Error detected at iteration {i}"