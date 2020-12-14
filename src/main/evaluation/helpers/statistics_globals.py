
# FIXME check if all fields are up to date

config_columns_except_seed = {
    "cell-k",
    "cell-max-active-inp",
    "create-inp-starting-time",
    "flowSchedulerPostponeSchedulingIfStuck",
    "hireFeasibleArcsDepth",
    "hireFlavorDeactivationTrigger",
    "hireForceServerFlavorIfNoFlavorHasOption",
    "hireHackedNodeSupply",
    "hireInpServerPenaltyCost",
    "hireInpServerPenaltyWaitingLower",
    "hireInpServerPenaltyWaitingUpper",
    "hireLocalityModeM2N",
    "hireLocalityModeNTG2N",
    "hireLocalityModeSTG2N",
    "hireMissingResourceThreshold",
    "hirePreemptionTakeBatchOfCandidates",
    "hirePreventHighLoadSolver",
    "hirePropagateDownstreamServerLocality",
    "hireShortcutsMaxSearchSpace",
    "hireShortcutsMaxSelection",
    "hireThresholdPreemptionCandidatesForceServer",
    "inp-types",
    "kappa-draw-random",
    "kappa-runtime",
    "kappa-tasks",
    "max-server-capacity",
    "max-switch-capacity",
    "maxInpFlavorDecisionsPerRound",
    "maxPreemptionBeforeServer",
    "maxServerPressure",
    "minQueuingTimeBeforePreemption",
    "mu-inp",
    "precision",
    "cellSwitchHomogeneous",
    "ratioOfIncTaskGroups",
    "scale-cell-servers",
    "scale-cell-switches",
    "scheduler",
    "shared-resource-mode",
    "sim-time",
    "workload-time",
    "softLimitProducersInGraph",
    "sspMaxSearchTimeSeconds",
    "statistics-start",
    "status-report-message",
    "think-time-scaling",
    "disableLimits"
}

# Statistics columns that shall be interpreted as integers
int_columns = [
    "sim-time",
    "statistics-interval",
    "max-server-capacity",
    "cell-k",
    "cell-max-active-inp",
    # From solver statistics
    "RunID",
    "SimulationTime",
    "StartTimeNanos",
    "EndTimeNanos",
    "ProducerCnt",
    "NonProducerCnt",
    "Supply",
    # From tenant statistics
    "JobID",
    "TaskGroupID",
    "SubmissionTime",
    "TotalTasks",
    "TasksStarted",
    "PlacementLatency",
    "Duration",
    "OriginalDuration",
    "InvolvedTGCnt",
    "TasksTotal",
    "TasksStarted",
    # From cell statistics
    "Time",
    # From scheduler statistics
    "Attempts",
    "Allocations",
    "ScheduledTasks",
    "ThinkTime",
    "ThinkTimeWasted",
    "JobsInQueue",
    "TotalJobsFullyScheduled",
    "TotalJobsFullyScheduledINP",
    "TotalJobQueueTime",
    "CountJobs",
    "CountJobsFinished",
    "CountJobsFinishedINP",
    "CountPreemptions",
    "PendingSchedulingItems",
    "PendingJobsNotFullyScheduled",
    "PendingJobsFullyScheduled",
    "PendingJobsNotFullyScheduledPlusFutureTgSubmissions",
    "TimesServerFallbackResubmit",
    "TimesServerFlavorTaken",
    "TimesSwitchFlavorTaken"
]

bool_columns = [
    "flow-scheduler-take-real-think-time",
    "hirePreventHighLoadSolver",
    "hirePropagateDownstreamServerLocality",
    "kappa-draw-random",
    "hirePostponePreemptionOnFeasibleJobAllocation",
    "hirePostponePreemptionOnOverloadedCell",
    "useSimpleTwoStateInpServerFlavorOptions"
]

# Statistics Columns that shall be interpreted as floating point numbers
float_columns = [
    "mu-inp",
    "think-time-scaling",
    # From tenant statistics
    "AvgQueueing",
    "AvgTaskQueueing",
    "AvgTaskDuration",
    "AvgTaskDurationOriginal",
    # From cell statistics (only respects 2 resource dimensions)
    "UtilizationSwitchINP",
    "UtilizationSwitchesDim1",
    "UtilizationSwitchesDim2",
    "UtilizationSwitchesDim3",
    "ActualUtilizationSwitchesDim1",
    "ActualUtilizationSwitchesDim2",
    "ActualUtilizationSwitchesDim3",
    "UtilizationServerDim1",
    "UtilizationServerDim2",
    'DetourInc',
    'InvolvedRacks',
    'MaxDiameter'
]
