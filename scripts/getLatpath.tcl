set target_pins [get_pins -regexp -hierarchical {.*puf_loop.*Q_reg/D.*} ]
# report_property [get_timing_paths -to puf_loop[0].puf_inst/dl0/Q_reg/D]

set fh [open "H:/PUF/PUF_manualPR/Nx_paths05sync.csv" w]

puts $fh "Pin From, Pin To, Datapath Delay (ps)"

foreach pin $target_pins {
    set path_delay [get_property DATAPATH_DELAY [get_timing_paths -to $pin ] ]
    set p_start [get_property STARTPOINT_PIN [get_timing_paths -to $pin ] ]
    puts $fh "$p_start, $pin, $path_delay"
}

close $fh
