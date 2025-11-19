from compilers.esperpiler_parallax import esperpile

pkt = esperpile("We are the quiet between heartbeats.", mode="ceremonial")
print(pkt.human_legible)
